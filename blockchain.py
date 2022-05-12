from block import Block

class Blockchain:
    blocks: list[Block]
    complexity: int

    def __init__(self, complexity):
        self.complexity = complexity
        genesis = Block("", None, complexity)
        self.blocks = [ genesis ]

    def add(self, data):
        b = Block(self.blocks[-1].hash, data, self.complexity)
        b.mine()
        self.blocks.append( b )

    def addMultiple(self, items):
        for item in items:
            self.add(item)

    def validate(self):
        for i in range(1, len(self.blocks)):
            if (not self.blocks[i].valid(self.blocks[i-1])):
                return False
        return True

    def search(self, hash):
        for b in self.blocks:
            if (b.hash == hash):
                return b
        return None
    
    def print(self):
        for i in range(len(self.blocks)):
            print(self.blocks[i])