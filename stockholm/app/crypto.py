"""
https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa/#key-serialization
"""
import secrets
import hashlib
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
    os.environ['STOCKHOLM_PRIVATE_KEY'] = filename
    return public_key

def generate_key():
    aes_key = generate_aes_key()
    private_key = generate_private_key()
    public_key = generate_public_key(private_key)

def generate_aes_key(is_create = False) -> Fernet:
    filename = 'aes.key'
    key = Fernet.generate_key()
    print(key)
    fernet = Fernet(key)
    log_info(key=f'{filename} ', message='has been generated')
    return fernet

def encrypt(filename: str):
    try:
        # public_key_filename = os.environ['STOCKHOLM_PUBLIC_KEY']
        public_key_filename = 'public-aes256.pem'
        with open(filename, 'rb') as original_file:
            original_data = original_file.read()
            with open(public_key_filename, 'rb') as public_key_file:
                public_key = serialization.load_pem_public_key(
                    public_key_file.read()
                )
                print(original_data)
                # print(public_key.public_bytes(
                #     encoding=serialization.Encoding.PEM,
                #     format=serialization.PublicFormat.SubjectPublicKeyInfo
                # ))
                
                print('isinstance:',  isinstance(public_key, rsa.RSAPublicKey))
                ciphertext = public_key.encrypt(
                    # original_data,
                    b"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum",
                    padding.OAEP(
                        mgf=padding.MGF1(algorithm=hashes.SHA256()),
                        algorithm=hashes.SHA256(),
                        label=None
                    )
                )
                print(ciphertext)
    except KeyError as e:
        log_error(f'INVALID KEY: {e}')
    # except Exception as e:
    #     print(e)