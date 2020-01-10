import sys
import base64
from Crypto import Random
from Crypto.Cipher import AES

class AESCipher(object):
    def __init__(self, key, block_size=32):
        self.bs = block_size
        if len(key) >= len(str(block_size)):
            self.key = key[:block_size]
        else:
            self.key = self._pad(key)
            