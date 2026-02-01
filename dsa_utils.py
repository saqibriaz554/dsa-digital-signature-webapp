from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.exceptions import InvalidSignature
import os

KEY_PATH = "keys"
PRIVATE_KEY_FILE = f"{KEY_PATH}/private.pem"
PUBLIC_KEY_FILE = f"{KEY_PATH}/public.pem"


def keys_exist():
    """Check if key files already exist."""
    return os.path.exists(PRIVATE_KEY_FILE) and os.path.exists(PUBLIC_KEY_FILE)


def generate_keys():
    """Generate DSA key pair and save to files."""
    os.makedirs(KEY_PATH, exist_ok=True)

    private_key = dsa.generate_private_key(key_size=2048)
    public_key = private_key.public_key()

    with open(PRIVATE_KEY_FILE, "wb") as f:
        f.write(
            private_key.private_bytes(
                serialization.Encoding.PEM,
                serialization.PrivateFormat.PKCS8,
                serialization.NoEncryption()
            )
        )

    with open(PUBLIC_KEY_FILE, "wb") as f:
        f.write(
            public_key.public_bytes(
                serialization.Encoding.PEM,
                serialization.PublicFormat.SubjectPublicKeyInfo
            )
        )


def sign_data(data):
    """Sign file data using private key."""
    with open(PRIVATE_KEY_FILE, "rb") as f:
        private_key = serialization.load_pem_private_key(f.read(), password=None)

    return private_key.sign(data, hashes.SHA256())


def verify_data(data, signature):
    """Verify signature using public key."""
    with open(PUBLIC_KEY_FILE, "rb") as f:
        public_key = serialization.load_pem_public_key(f.read())

    try:
        public_key.verify(signature, data, hashes.SHA256())
        return True
    except InvalidSignature:
        return False
