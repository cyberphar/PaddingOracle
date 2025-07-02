# examples/vulnerable_server.py

from flask import Flask, request, jsonify
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import binascii
import os

app = Flask(__name__)

KEY = os.urandom(16)
IV = os.urandom(16)

@app.route('/decrypt', methods=['POST'])
def decrypt():
    try:
        hex_data = request.get_data().decode()
        ciphertext = binascii.unhexlify(hex_data)
        if len(ciphertext) % 16 != 0:
            return "Invalid length", 400

        cipher = AES.new(KEY, AES.MODE_CBC, IV)
        plaintext = cipher.decrypt(ciphertext)

        # Test du padding (PKCS7)
        try:
            unpad(plaintext, 16)
            return "Valid padding", 200
        except ValueError:
            return "Invalid padding", 500  # ← comportement d'oracle
    except Exception as e:
        return f"Error: {str(e)}", 400

if __name__ == '__main__':
    print(f"[+] Server running on http://localhost:5000")
    app.run(host='0.0.0.0', port=5001)
