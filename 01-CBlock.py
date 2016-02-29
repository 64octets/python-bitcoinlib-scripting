### Open Provenance February 2016 - https://myveryown.org
### Bitcoin Blockchain Information using python-bitcoinlib
### CBlock Object and Properties
### Donate to Open Provenance: 1opDUZQ9nsL1LJALBdV1dvqSMtcvNj9EC

## Import the modules required
import bitcoin
import bitcoin.rpc

## Create a proxy object and connect to the bitcoin.rpc 
myproxy = bitcoin.rpc.Proxy()

## Get the latest CBlock data from bitcoin rpc proxy
block_info = myproxy.getblock(myproxy.getblockhash(myproxy.getblockcount()))

## Print the details to the screen.
print "----------------------------------------------------------------"
print "Bitcoin CBlock Object Information: Block Height ", myproxy.getblockcount()
print "----------------------------------------------------------------"
print "Block Difficulty: ", block_info.difficulty
print "Block nVersion: ", block_info.nVersion
print "Block nNonce: ", block_info.nNonce
print "Block nBits: ", block_info.nBits
print "Block nTime: ", block_info.nTime
print "No of Transactions: ", len(block_info.vtx)
print " "
print "Block Hash: "
print bitcoin.core.b2lx(block_info.GetHash())
print " " 
print "Previous Block Hash: "
print bitcoin.core.b2lx(block_info.hashPrevBlock)
print " " 
print "Merkel Root: "
print bitcoin.core.b2lx(block_info.hashMerkleRoot)
print ' ' 
print "----------------------------------------------------------------"
print "Dump of RAW CBlock Object:"
print block_info
print "----------------------------------------------------------------"
print ' ' 
exit()
