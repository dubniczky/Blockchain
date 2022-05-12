from datetime import datetime

from blockchain import Blockchain

def test_blockchain_empty():
    bc = Blockchain(2)
    assert bc.complexity == 2
    assert len(bc.blocks) == 1

def test_blockchain_adding():
    bc = Blockchain(2)
    bc.add(None)
    bc.add("heyo")
    bc.add(2)
    bc.add({'a': True})

    assert bc.blocks[1].data == None
    assert bc.blocks[2].data == "heyo"
    assert bc.blocks[3].data == 2
    assert bc.blocks[4].data == {'a': True}

def test_blockchain_validity():
    bc = Blockchain(2)
    bc.add(None)
    bc.add("heyo")
    bc.add(2)
    bc.add({'a': True})

    assert bc.validate()

def test_blockchain_invalidity():
    bc = Blockchain(2)
    bc.add(None)
    bc.add("heyo")
    bc.add(2)
    bc.add({'a': True})

    bc.blocks[1].data = '!'

    print(bc.blocks)

    assert not bc.validate()

def test_blockchain_search():
    bc = Blockchain(2)
    bc.add(None)
    bc.add("heyo")
    bc.add(2)
    bc.add({'a': True})

    h0 = bc.blocks[0].hash
    h3 = bc.blocks[3].hash
    h4 = bc.blocks[4].hash
    assert bc.search(h0).data == None
    assert bc.search(h3).data == 2
    assert bc.search(h4).data == {'a': True}
    assert bc.search('---') == None