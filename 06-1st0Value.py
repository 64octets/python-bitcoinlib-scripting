### Open Provenance March 2016 - https://myveryown.org
### Bitcoin Blockchain Information using python-bitcoinlib
### The First Zero Value Output Bitcoin Transaction
### Donate to Open Provenance: 1opDUZQ9nsL1LJALBdV1dvqSMtcvNj9EC

## In this script we search the blockchain for the first ever zero value output bitcoin transaction
## We do this by searching for the first valid output with a zero value

## Hint 
## Block Number: 82627
## TX 2f2442f68e38b980a6c4cec21e71851b0d8a5847d85208331a27321a9967bbd6


## Import the modules required and setup a connection to bitcoin
import bitcoin

## Create a proxy object and connect to the bitcoin.rpc 
import bitcoin.rpc
myproxy = bitcoin.rpc.Proxy()

## Declare some variables used by our search
starting_block = 0
ending_block = myproxy.getblockcount()

print "Searching for the 1st Zero Value Transaction ..."

## Now search block by block until we find what we are looking for
for blockno in range (starting_block, ending_block) :
	# print blockno	
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
							print "Block Number:", blockno
							print "TX "
							print bitcoin.core.b2lx(thetx.GetHash())
							## OK we have finished
							exit()