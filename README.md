# dsa-digital-signature-webapp
A Flask-based web application implementing the Digital Signature Algorithm (DSA) to sign and verify files using SHA-256 for integrity and authentication.
🔐 DSA Digital Signature Web Application

This project is a web-based implementation of the Digital Signature Algorithm (DSA) built using Python Flask and the Cryptography library. The system allows users to generate cryptographic keys, digitally sign files, and verify file authenticity through digital signatures.

The application demonstrates how modern cryptographic systems ensure:

Integrity — Files cannot be altered without detection

Authentication — Confirms the identity of the signer

Non-Repudiation — Signer cannot deny signing the file

🚀 Features

🔑 Generates 2048-bit DSA key pair

✍️ Digitally signs uploaded files using the private key

✔ Verifies signatures using the public key

🔒 Uses SHA-256 hashing

🌐 Simple Flask web interface

⚠ Auto-detects missing keys and generates them

🛠 Technologies Used
Technology	Purpose
Python	Backend programming
Flask	Web framework
Cryptography Library	DSA implementation
HTML/CSS	Frontend interface
📚 Educational Purpose

This project is designed for learning and demonstration of digital signatures in cybersecurity and cryptography courses. It provides hands-on understanding of how public-key cryptography is used in real-world systems like:

Software signing

Secure emails

Blockchain transactions

SSL/TLS certificates

🔍 How It Works

User uploads a file

System signs the file using private key

Signature is generated as hexadecimal string

Verification checks signature using public key

System confirms whether the file is authentic or modified

⚠ Important Note

This project focuses on digital signatures, not encryption.
It ensures authenticity and integrity, but does not hide data.

👨‍💻 Author

Saqib Riaz
Cyber Security & Digital Forensics Graduate
