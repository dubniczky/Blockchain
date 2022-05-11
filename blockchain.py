from block import Block

class Blockchain:
    blocks: list[Block]
    complexity: int

    def __init__(self, complexity):
        self.complexity = complexity
        genesis = Block("", None)
        self.blocks = [ genesis ]

    def add(self, data):
        b = Block(self.blocks[-1].hash, data)
        b.mine(complexity=self.complexity)
        self.blocks.append( b )

    def validate(self):
        for i in range(1, len(self.blocks)):
            if (not self.blocks[i].isValid() or self.blocks[i-1].hash != self.blocks[i].previous_hash):
                return False
        return True