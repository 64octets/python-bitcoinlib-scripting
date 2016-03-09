### Open Provenance March 2016 - https://myveryown.org
### Bitcoin Blockchain Information using python-bitcoinlib
### The First Block with OP_RETURN
### Donate to Open Provenance: 1opDUZQ9nsL1LJALBdV1dvqSMtcvNj9EC

## In this script we search the blockchain for the first OP_RETURN bitcoin transaction
## We do this by searching for the first valid output with a zero value and where
## the first 2 chars of the script sig are '6a', 
## we then drop those and the next two (which indicate size) and then display the rest of the data

## scriptSig Transaction Hex
## 6a = OP_RETURN

## Hint 
##
## Block Number: 228596
## TX:  eb31ca1a4cbd97c2770983164d7560d2d03276ae1aee26f12d7c2c6424252f29
## scriptSig: 6a
## OP_RETURN:
##
## Block Number: 228596
## TX:  3d665c1eb25160444cf053988a0d7d0c3ec5e68e3897a917d59447052788cfc5
## scriptSig: 6a
## OP_RETURN:
##
## Block Number: 228596
## TX:  1a2e22a717d626fc5db363582007c46924ae6b28319f07cb1b907776bd8293fc
## scriptSig: 6a14215477656e74792062797465206469676573742e
## OP_RETURN:  215477656e74792062797465206469676573742e
## scriptSig: j!Twenty byte digest.


## Import the modules required and setup a connection to bitcoin
import bitcoin

## Create a proxy object and connect to the bitcoin.rpc 
import bitcoin.rpc
myproxy = bitcoin.rpc.Proxy()

## Declare some variables used by our search
starting_block = 228595
ending_block = myproxy.getblockcount()

print "Searching for the 1st Block with OP_RETURN ..."

## Setup a flag we use to control the search exit - as there may be more than one OP_RETURN in initial block with an OP_RETURN
OPRETURN_FOUND = False

## Now search block by block until we find what we are looking for
for blockno in range (starting_block, ending_block) :
	
	block_info = myproxy.getblock(myproxy.getblockhash(blockno))
	vtx = block_info.vtx
	tx_count = len(block_info.vtx)
	if tx_count >= 2 : # then we have more than just a coinbase transaction in the current block
  		for x in range (0, len(vtx)) :  
			thetx = vtx[x] #grab the CTransaction object 
			vout = thetx.vout #grab the CTxOut object
			if len(vout) >= 1 : 
				for o in range (0, len(vout)) :
					vo = vout[o]
					if vo.is_valid() :
						if vo.nValue == 0 :
							x = bitcoin.core.b2x(vo.scriptPubKey)
							if x[:2] == "6a" :
								print "Block Number:", blockno
								print "TX: ", bitcoin.core.b2lx(thetx.GetHash())
								print "scriptPubKey: ", bitcoin.core.b2x(vo.scriptPubKey)
								print vo.scriptPubKey
								print "OP_RETURN: ", x[4:] 
								OPRETURN_FOUND = True
								## OK we have finished
	if OPRETURN_FOUND :
		exit() ## we exit at the end of a block
		