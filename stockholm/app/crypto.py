"""
https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa/#key-serialization
"""
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey, RSAPublicKey
from logger import log_info, log_title, log_error


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
    filename = os.environ.get('STOCKHOLM_PRIVATE_KEY', 'private.pem')
    write_file(filename, 'wb', private_pem)
    return private_key

def load_private_key() -> RSAPrivateKey:
    try:
        private_key_filename = os.environ.get('STOCKHOLM_PRIVATE_KEY', 'private.pem')
        with open(private_key_filename, 'rb') as private_key_file:
            private_key = serialization.load_pem_private_key(
                private_key_file.read(),
                password=None
            )
            log_info('private key loaded')
            return private_key
    except Exception as e:
        log_error('Error Loading Private key')

def generate_public_key(private_key: RSAPrivateKey) -> RSAPublicKey:
    public_key = private_key.public_key()
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    filename = os.environ.get('STOCKHOLM_PUBLIC_KEY', 'public.pem')
    write_file(filename, 'wb', public_pem)
    return public_key

def load_public_key() -> RSAPublicKey:
    try:
        public_key_filename = os.environ.get('STOCKHOLM_PUBLIC_KEY', 'public.pem')
        with open(public_key_filename, 'rb') as public_key_file:
            public_key = serialization.load_pem_public_key(
                public_key_file.read()
            )
            log_info('public key loaded')
            return public_key
    except Exception as e:
        log_error('Error Loading Public key')

def generate_symmetric_key() -> Fernet:
    filename = os.environ.get('STOCKHOLM_SYMMETRIC_KEY', 'symmetric.pem')
    symmetric_key = Fernet.generate_key()
    fernet = Fernet(symmetric_key)
    write_file(filename, 'wb', symmetric_key)
    return fernet

def load_symmetric_key() -> Fernet:
    try:
        log_info('loadding symmetric key')
        symmetric_key_filename = os.environ.get('STOCKHOLM_SYMMETRIC_KEY', 'symmetric.pem')
        with open(symmetric_key_filename, 'rb') as symmetric_key_file:
            symmetric_key = symmetric_key_file.read()
        fernet = Fernet(symmetric_key)
        log_info('symmetric key loaded')
        return fernet
    except Exception as e:
        log_error('Error Loading Symmetric key')

def encrypt_symmetric_key():
    try:
        symmetric_key_filename = os.environ.get('STOCKHOLM_SYMMETRIC_KEY', 'symmetric.pem')
        with open(symmetric_key_filename, 'rb') as symmetric_key_file:
            symmetric_key = symmetric_key_file.read()
        public_key = load_public_key()
        if not public_key:
            return
        ciphertext = public_key.encrypt(
            symmetric_key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        hybrid_key_filename = os.environ.get('STOCKHOLM_HYBRID_KEY', 'hybrid.pem')
        write_file(hybrid_key_filename, 'wb', ciphertext)
    except Exception as e:
        log_error('Encrypt Symmetric Key Error: could not load symmetric key')

def decrypt_symmetric_key():
    try:
        hybrid_key_filename = os.environ.get('STOCKHOLM_HYBRID_KEY', 'hybrid.pem')
        symmetric_key_filename = os.environ.get('STOCKHOLM_SYMMETRIC_KEY', 'symmetric.key')
        with open(hybrid_key_filename, 'rb') as hybrid_key_file:
            ciphertext = hybrid_key_file.read()
        private_key = load_private_key()
        symmetric_key = private_key.decrypt(
            ciphertext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        write_file(symmetric_key_filename, 'wb', symmetric_key)
    except Exception as e:
        log_error('Decrypt Symmetric Key Error: could not load private key')

def write_file(filename: str, mode: str, data: any):
    if os.path.dirname(filename):
        os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, mode=mode) as f:
        f.write(data)
    log_info(key=f'{filename} ', message='has been created')
