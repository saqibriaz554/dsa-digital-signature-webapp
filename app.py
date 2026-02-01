from flask import Flask, render_template, request
from dsa_utils import generate_keys, sign_data, verify_data, keys_exist
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def index():
    msg, sig = "", ""

    if request.method == "POST":
        action = request.form.get("action")

        # Ensure keys exist before signing/verifying
        if action in ["sign", "verify"] and not keys_exist():
            generate_keys()
            msg = "Keys were missing — new keys generated."

        # Handle file safely
        file = request.files.get("file")
        if not file:
            return render_template("index.html", msg="No file uploaded!", sig="")

        data = file.read()

        if action == "generate":
            generate_keys()
            msg = "DSA Keys Generated Successfully"

        elif action == "sign":
            signature = sign_data(data)
            sig = signature.hex()
            msg = "File Signed Successfully"

        elif action == "verify":
            sig_input = request.form.get("signature", "").strip()
            if not sig_input:
                msg = "Please provide a signature to verify"
            else:
                try:
                    result = verify_data(data, bytes.fromhex(sig_input))
                    msg = "✅ Signature VALID" if result else "❌ Signature INVALID"
                except ValueError:
                    msg = "Invalid signature format"

    return render_template("index.html", msg=msg, sig=sig)


if __name__ == "__main__":
    app.run(debug=True)
