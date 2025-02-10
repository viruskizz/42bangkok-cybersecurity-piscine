"""
https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa/#key-serialization
"""
from logger import log_info, log_title
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

def generate_pem_key():
    """ Generate private key as PEM serialize without any encrypted """
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )
    with open('private.pem', 'wb') as private_pem_file:
        private_pem_file.write(private_pem)

# BestEncryption is AES256
# https://stackoverflow.com/questions/61166493/which-encryption-algorithm-do-serialization-bestavailableencryptionbmypassword
def generate_pem_aes_key():
    """ Generate private key as PEM serialize with AES encrypted """
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    private_pem_encrypted = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.BestAvailableEncryption(b'mypassword')
    )
    with open('private-aes256.pem', 'wb') as private_pem_aes_file:
        private_pem_aes_file.write(private_pem_encrypted)
