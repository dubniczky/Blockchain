from datetime import datetime
from blockchain import Block

def test_block_empty():
    b = Block("", None, 2)
    assert b.previous_hash == "" 
    assert b.data == None
    assert b.proof == 0

def test_block_previous():
    b1 = Block("", None, 2)
    b2 = Block(b1.hash, None, 2)

    assert b1.hash == b2.previous_hash

def test_block_mine():
    complexity = 2
    b1 = Block("", {'var': 'val'}, complexity, time=datetime(1997, 11, 27, 11, 32, 23, 19233))
    b2 = Block(b1.hash, {'item': 13_556}, complexity, time=datetime(1993, 3, 12, 10, 0, 3, 234))
    b3 = Block(b2.hash, {}, complexity, time=datetime(2000, 1, 1, 0, 0, 0, 3234))

    b2.mine()
    b3.mine()

    assert b2.hash.startswith('0' * complexity)
    assert b3.hash.startswith('0' * complexity)

def test_block_validity():
    complexity = 2
    b1 = Block("", {'var': 'val'}, complexity, time=datetime(1997, 11, 27, 11, 32, 23, 19233))
    b2 = Block(b1.hash, {'item': 13_556}, complexity, time=datetime(1993, 3, 12, 10, 0, 3, 234))
    b3 = Block(b2.hash, {}, complexity, time=datetime(2000, 1, 1, 0, 0, 0, 3234))

    b2.mine()
    b3.mine()

    assert b1.valid()
    assert b2.valid()
    assert b3.valid()

    b2.data = {'item': 13_555}

    assert not b2.valid()