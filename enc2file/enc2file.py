# -*- coding: utf-8 -*-
from cryptography.fernet import Fernet


class Enc2File:

    def __init__(self, key=None, encoding='utf-8'):
        self.encoding = encoding
        if key is None:
            key = Fernet.generate_key()
        else:
            key = self.str2token(key)
        self._key_ = key
        self.fernet = Fernet(key)

    def get_encryption_key(self):
        return self.token2str(self._key_)

    def set_encryption_key(self, key):
        key = self.str2token(key)
        self._key_ = key
        self.fernet = Fernet(key)

    def get_encoding(self):
        return self.encoding

    def set_encoding(self, encoding):
        self.encoding = encoding

    def token2str(self, token):
        # Returns a string encoded with encoding of the object, from the received bytes token.
        return str(token, self.encoding)

    def str2token(self, message):
        # Returns a bytes token from the received string, encoded with encoding of the object.
        return bytes(message.encode(self.encoding))

    def encrypt(self, message):
        # Returns an encrypted str of the received str message, using the encryption key of the object.
        return self.token2str(self.fernet.encrypt(self.str2token(message)))

    def decrypt(self, enc_text):
        # Returns the decrypted str of the received encrypted str, using the encryption key of the object.
        return self.token2str(self.fernet.decrypt(self.str2token(enc_text)))

    def key_to_file(self, target_file_path):
        # Stores the string representation of the current key in target file.
        try:
            with open(target_file_path, 'w') as fh:
                fh.write(self.token2str(self._key_))
        except IOError:
            print('File {} could not be accessed.'.format(target_file_path))

    def key_from_file(self, target_file_path):
        # Sets the current key to the one read from target file.
        try:
            with open(target_file_path, 'r') as fh:
                self.set_encryption_key(fh.read())
        except IOError:
            print('File {} could not be accessed.'.format(target_file_path))

    def enc2file(self, message, target_file_path):
        # Writes encrypted message string to a file.
        try:
            with open(target_file_path, 'w') as fh:
                fh.write(self.encrypt(message))
        except IOError:
            print('File {} could not be accessed.'.format(target_file_path))

    def decrypt_from_file(self, target_file_path):
        # Returns the decrypted string of the encrypted text read from a file.
        try:
            with open(target_file_path, 'r') as fh:
                return self.decrypt(fh.read())
        except IOError:
            print('File {} could not be accessed.'.format(target_file_path))
