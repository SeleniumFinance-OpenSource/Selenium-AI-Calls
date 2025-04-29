from cryptography.hazmat.primitives.ciphers.aead import AESGCM

class AESGCMEncryption:
    def __init__(self, config):
        self.config = config

    def encrypt_attachment(self, data, key):
        aesgcm = AESGCM(key)
        nonce = os.urandom(12)
        ciphertext = aesgcm.encrypt(nonce, data, None)
        return nonce + ciphertext
