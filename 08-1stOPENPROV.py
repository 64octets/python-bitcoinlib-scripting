### Open Provenance March 2016 - https://myveryown.org
### Bitcoin Blockchain Information using python-bitcoinlib
### The First OPENPROV Bitcoin Transaction
### Donate to Open Provenance: 1opDUZQ9nsL1LJALBdV1dvqSMtcvNj9EC

## In this script we search the blockchain for the first OPENPROV prefixed OP_RETURN bitcoin transaction
## We do this by searching for the first valid output with a zero value and where
## the first 2 chars of the script sig are '6a', 
## we then drop those and the next two (which indicate size) and then if we find 4f50454e50524f56
## which is OPENPROV then we display the SHA256 

## Transaction Hex
# 6a = OP_RETURN
# 4f50454e50524f56 = OPENPROV

## Hint 
## Block: 371679
## TX: 47aa7391eede3049d0dbc14ff356c0cd82f4ca1149062a4734d7fc44ec86802c
## OP_RETURN: 4f50454e50524f56de4dfb0084b79c7611e31ae44cfb2cc027680caa3d713c7614d4b7508f6b79be
## SHA256: de4dfb0084b79c7611e31ae44cfb2cc027680caa3d713c7614d4b7508f6b79be

## Import the modules required and setup a connection to bitcoin
import bitcoin

## Create a proxy object and connect to the bitcoin.rpc 
import bitcoin.rpc
myproxy = bitcoin.rpc.Proxy()

## Declare some variables used by our search
starting_block = 371678
print starting_block
ending_block = myproxy.getblockcount()
print ending_block
print "Searching for the 1st OPENPROV OP_RETURN Transaction ..."

## Setup a flag we use to control the search exit - as there may be more than one OP_RETURN in initial block with an OP_RETURN
OPENPROV_FOUND = False

## Now search block by block until we find what we are looking for
for blockno in range (starting_block, ending_block) :
	isopr = 0
	block_info = myproxy.getblock(myproxy.getblockhash(blockno))
	vtx = block_info.vtx
	tx_count = len(block_info.vtx)
	print blockno, tx_count
	if tx_count >= 2 : # then we have more than just a coinbase transaction in the current block
  		for x in range (0, len(vtx)) :  #loop the transactions
			thetx = vtx[x] #grab the CTransaction object 
			vout = thetx.vout #grab the CTxOut object
			if len(vout) >= 1 : # 
				for o in range (0, len(vout)) :
					vo = vout[o]
					if vo.is_valid() :
						if vo.nValue == 0 :
							x = bitcoin.core.b2x(vo.scriptPubKey)
							if x[:2] == "6a" :
								isopr = isopr+1
								opr_data = x[4:]
								if opr_data[:16] == "4f50454e50524f56" :
									print "Block Number:", blockno
									print "TX "
									print bitcoin.core.b2lx(thetx.GetHash())
									print "OP_RETURN"
									print x[4:]
									print "OPENPROV"
									print "SHA256 ", opr_data[16:]
									print bitcoin.core.b2x(vo.scriptPubKey)
									OPENPROV_FOUND = True
									## OK we have finished
		print "OP_RETURNS:", isopr
	if OPENPROV_FOUND :
		exit() ## we exit at the end of a block