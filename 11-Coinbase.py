### Open Provenance February 2016 - https://myveryown.org
### Bitcoin Blockchain Information using python-bitcoinlib
### The most recent 50 Coinbase Messages 
### Donate to Open Provenance: 1opDUZQ9nsL1LJALBdV1dvqSMtcvNj9EC

## Import the modules required and setup a connection to bitcoin
import bitcoin

## Create a proxy object and connect to the bitcoin.rpc 
import bitcoin.rpc
myproxy = bitcoin.rpc.Proxy()

## Declare some variables used by our search
ending_block = myproxy.getblockcount()
starting_block = ending_block - 50
#block = 0 Satoshi Message

## Now search block by block until we find what we are looking for
for blockno in range (starting_block, ending_block) :
	block_info = myproxy.getblock(myproxy.getblockhash(blockno))
	## Grab the transactions from the block
	vtx = block_info.vtx
	#'# Grab the CTransaction object from the block 
	thetx = vtx[0] 
	## From the CTransaction Object we get the CTxIn Objects
	vin = thetx.vin
	## Grab the COutPoint or Previous Input Object 
	vi = vin[0] 

	## Grab the scriptSig  
	vip = vi.scriptSig
	
	print blockno, vip
