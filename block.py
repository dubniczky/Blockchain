from datetime import datetime
from hashlib import sha256

class Block:
    data: object
    hash: str
    previous_hash: str
    time: datetime
    proof: int

    def __init__(self, previous_hash: str, data: object, *, time = datetime.now()):
        self.previous_hash = previous_hash
        self.data = data
        self.time = time
        self.proof = 0
        self.hash = self.sha256()
    
    def sha256(self):
        block = [
            self.previous_hash, ';',
            str(self.time), ';',
            str(self.data), ';',
            str(self.proof), ';',
        ]
        return sha256(''.join(block).encode('utf8')).hexdigest()

    def valid(self):
        return self.sha256() == self.hash

    def mine(self, complexity):
        prefix = '0' * complexity
        while not self.hash.startswith(prefix):
            self.proof += 1
            self.hash = self.sha256()

    def __str__(self):
        block = [
            '{\n   ',
            'Hash: ', str(self.hash), '\n   ',
            'Prev: ', str(self.previous_hash), '\n   ',
            'Time: ', str(self.time), '\n   ',
            'Data: ', str(self.data), '\n   ',
            'Prof: ', str(self.proof), '\n',
            '}',
        ]
        return ''.join(block)