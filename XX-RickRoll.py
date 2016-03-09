### Open Provenance March 2016 - https://myveryown.org
### Bitcoin Blockchain Information using python-bitcoinlib
### Blockchain RickRoll 
### Donate to Open Provenance: 1opDUZQ9nsL1LJALBdV1dvqSMtcvNj9EC

## Import the modules required and setup a connection to bitcoin
import bitcoin

## Create a proxy object and connect to the bitcoin.rpc 
import bitcoin.rpc
myproxy = bitcoin.rpc.Proxy()

## The TX that contains the RickRoll 
mytx = "d29c9c0e8e4d2a9790922af73f0b8d51f0bd4bb19940d9cf910ead8fbe85bc9b"

##Convert from little endian hex to binary
mytxb = bitcoin.core.lx(mytx)

print "Loading the Rick Roll OP_RETURN ..."
print "Block Number: 268060"
print "TX:", mytx

## Load the TX and 
tx_info = myproxy.getrawtransaction(mytxb)
vout = tx_info.vout #grab the CTxOut object
if len(vout) >= 1 : 
	for o in range (0, len(vout)) :
		vo = vout[o]
		print vo.scriptPubKey
		exit() ## we exit at the end of a block