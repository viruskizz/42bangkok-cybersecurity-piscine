"""
https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa/#key-serialization
"""
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey, RSAPublicKey
from logger import log_info, log_title, log_error

def encrypt_file(filename: str):
    try:
        with open(filename, 'rb') as original_file:
            original_data = original_file.read()
            print(original_data)
    except KeyError as e:
        log_error(f'INVALID KEY: {e}')
    except Exception as e:
        print(e)

def generate_private_key() -> RSAPrivateKey:
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
    filename = 'private.pem'
    with open(filename, 'wb') as private_pem_file:
        private_pem_file.write(private_pem)
    log_info(key=f'{filename} ', message='has been generated')
    os.environ['STOCKHOLM_PRIVATE_KEY'] = filename
    return private_key

def generate_public_key(private_key: RSAPrivateKey) -> RSAPublicKey:
    public_key = private_key.public_key()
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    filename = 'public.pem'
    with open(filename, 'wb') as private_pem_aes_file:
        private_pem_aes_file.write(public_pem)
    log_info(key=f'{filename} ', message='has been generated')
    os.environ['STOCKHOLM_PUBLIC_KEY'] = filename
    return public_key

def generate_symmetric_key() -> Fernet:
    filename = 'symmetric.key'
    symmetric_key = Fernet.generate_key()
    fernet = Fernet(symmetric_key)
    with open(filename, 'wb') as symmetric_key_file:
        symmetric_key_file.write(symmetric_key)
    log_info(key=f'{filename} ', message='has been generated')
    os.environ['STOCKHOLM_SYMMETRIC_KEY'] = filename
    return fernet

def load_public_key(filename = None) -> RSAPublicKey:
    public_key_filename = filename if filename else os.environ['STOCKHOLM_PUBLIC_KEY']
    with open(public_key_filename, 'rb') as public_key_file:
        public_key = serialization.load_pem_public_key(
            public_key_file.read()
        )
        return public_key

def load_private_key(filename = None) -> RSAPrivateKey:
    private_key_filename = filename if filename else os.environ['STOCKHOLM_PRIVATE_KEY']
    with open(private_key_filename, 'rb') as private_key_file:
        private_key = serialization.load_pem_private_key(
            private_key_file.read()
        )
        return private_key

def load_symmetric_key(filename = None) -> Fernet:
    symmetric_key_filename = filename if filename else os.environ['STOCKHOLM_SYMMETRIC_KEY']
    with open(symmetric_key_filename, 'rb') as symmetric_key_file:
        symmetric_key = symmetric_key_file.read()
        fernet = Fernet(symmetric_key)
        return fernet