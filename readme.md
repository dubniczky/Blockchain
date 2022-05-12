# Python Blockchain

A simple transactional blockchain implemented in python

[[_TOC_]]

## Methodology

The blockchain consists of blocks represented by class objects. Each object has inherit values visible in the examples. Before mining a block, the hash of the previously mined block is added to the current block to establish the chain. Each block's hash has to start with a certain number of zero hex values in order to be considered valid. This is achieved through trial and error by iterating the proof variable.

## Usage Example

```python
from blockchain import Blockchain

bc = Blockchain(5) # Complexity
bc.add({'from': 'user1', 'to': 'user2', 'amount': 122.85})
bc.add({'from': 'user2', 'to': 'user1', 'amount': 4.99})
print(bc.validate())
bc.print()
```

## Example Blockchain

```yml
{
   Hash: 5aae8d94cf30107802641bb3f44483a6740900be133410425996f5106572ac34
   Prev:
   Time: 2022-05-12 02:29:17.928376
   Data: None
   Prof: 0
   Comp: 3
}
{
   Hash: 00038eceacbfad7d8c55116c6bf1c23c09196b61645a1c190c274c610c0cc0a3
   Prev: 5aae8d94cf30107802641bb3f44483a6740900be133410425996f5106572ac34
   Time: 2022-05-12 02:29:17.928376
   Data: None
   Prof: 151
   Comp: 3
}
{
   Hash: 0003c46ac8f27e17ec8110a0a90e56236ef5746a99d0c71dec6353ac86eb7809
   Prev: 00038eceacbfad7d8c55116c6bf1c23c09196b61645a1c190c274c610c0cc0a3
   Time: 2022-05-12 02:29:17.928376
   Data: heyo
   Prof: 977
   Comp: 3
}
{
   Hash: 000aa2be0eebbd3964c26daba9ba6e8a34e25ff82dac516e959582030ad9a3e4
   Prev: 0003c46ac8f27e17ec8110a0a90e56236ef5746a99d0c71dec6353ac86eb7809
   Time: 2022-05-12 02:29:17.928376
   Data: 2
   Prof: 12991
   Comp: 3
}
{
   Hash: 00021d76b6b34f021a98618d8a958606d0dd84ec9cd5567db1270624db7237b4
   Prev: 000aa2be0eebbd3964c26daba9ba6e8a34e25ff82dac516e959582030ad9a3e4
   Time: 2022-05-12 02:29:17.928376
   Data: {'a': True}
   Prof: 740
   Comp: 3
}
```
