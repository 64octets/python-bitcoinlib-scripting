### Open Provenance February 2016 - https://myveryown.org
### Bitcoin Blockchain Information using python-bitcoinlib
### CTransaction Object and Properties
### Donate to Open Provenance: 1opDUZQ9nsL1LJALBdV1dvqSMtcvNj9EC

## Import the modules required
import bitcoin
import bitcoin.rpc

## Create a proxy object and connect to the bitcoin.rpc 
myproxy = bitcoin.rpc.Proxy()

## Get the latest CBlock data from bitcoin rpc proxy
block_info = myproxy.getblock(myproxy.getblockhash(myproxy.getblockcount()))

## From the CBlock object we are able to get the transactions
vtx = block_info.vtx

## Print the details to the screen.
print "----------------------------------------------------------------"
print "Bitcoin CTransaction Object Information: Block Height ", myproxy.getblockcount()
print "----------------------------------------------------------------"

## We assume there could be many transactions in a block and loop through them
## we would loop all transaction with 'for x in range (0, len(vtx)) :'
## but in this example we will show the first or "coinbase" transaction details.

if len(vtx) > 0 :
  for x in range (0, 1) :

	## Isolate the CTransaction Object
	thetx = vtx[x]

	## Now we have the object we can get information from it
	print "Is Coinbase: ", thetx.is_coinbase()
	print "nVersion: ", thetx.nVersion
	print "nLockTime: ", thetx.nLockTime
	print "TxHash: "
	print bitcoin.core.b2lx(thetx.GetHash())
print "----------------------------------------------------------------"
print "Dump of RAW CTransaction Object:"
print thetx
print "----------------------------------------------------------------"
print ' ' 
exit()
