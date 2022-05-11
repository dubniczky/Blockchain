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
        b.mine(complexity=self.complexity)
        self.blocks.append( b )

    def validate(self):
        for i in range(1, len(self.blocks)):
            if (not self.blocks[i].valid(self.blocks[i-1])):
                return False
        return True