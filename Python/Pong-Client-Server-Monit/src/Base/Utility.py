import base64
import random

from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

# Encrypt methods

def KeyGenerator_Asymmetric():
    random = Random.new().read
    RSAkey = RSA.generate(1024, random)
    public = RSAkey.publickey().exportKey()
    private = RSAkey.exportKey()
    return public, private


def KeyGenerator_symmetric():
    key = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
    return key


class AESHandler:

    def __init__(self, name) -> None:
        super().__init__()
        self.key = KeyGenerator_symmetric()

    BS = AES.block_size  # 16 byte
    MODE = AES.MODE_CBC
    pad = lambda s: s + (AESHandler.BS - len(s) % AESHandler.BS) * chr(AESHandler.BS - len(s) % AESHandler.BS)
    unpad = lambda s: s[:-ord(s[-1])]

    # encrypt
    def enc(self, msg):
        iv = Random.new().read(AESHandler.BS)
        cipher = AES.new(self.key, AESHandler.MODE, iv)

        msg = AESHandler.pad(msg)
        c = cipher.encrypt(msg)
        msg = iv + c

        return base64.b64encode(msg)

    # decrypt
    def dec(self, msg):
        msg = base64.b64decode(msg)
        iv = msg[:AESHandler.BS]
        decipher = AES.new(self.key, AESHandler.MODE, iv)
        p = AESHandler.unpad(decipher.decrypt(msg[AESHandler.BS:]))
        return p


class PKCSHandler:

    def __init__(self, name) -> None:
        super().__init__()
        self.pubkey, self.prikey = KeyGenerator_Asymmetric()

    def enc(self, msg):
        ekey = RSA.importKey(open(self.pubkey).read())
        cipher = PKCS1_OAEP.new(ekey)
        ciphertext = cipher.encrypt(msg)
        return ciphertext

    def dec(self, msg):
        dkey = RSA.importKey(open(self.prikey).read())
        cipher = PKCS1_OAEP.new(dkey)
        msg = cipher.decrypt(msg)
        return msg
