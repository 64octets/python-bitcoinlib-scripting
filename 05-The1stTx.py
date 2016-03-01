### Open Provenance February 2016 - https://myveryown.org
### Bitcoin Blockchain Information using python-bitcoinlib
### The First Bitcoin Transaction
### Donate to Open Provenance: 1opDUZQ9nsL1LJALBdV1dvqSMtcvNj9EC

## In this script we search the blockchain for the first ever bitcoin transaction

## Import the modules required and setup a connection to bitcoin
import bitcoin

## Create a proxy object and connect to the bitcoin.rpc 
import bitcoin.rpc
myproxy = bitcoin.rpc.Proxy()

## Declare some variables used by our search
starting_block = 0
ending_block = myproxy.getblockcount()

print "Searching for the 1st Transaction ..."

## Now search block by block until we find what we are looking for
for blockno in range (starting_block, ending_block) :
	
	block_info = myproxy.getblock(myproxy.getblockhash(blockno))
	vtx = block_info.vtx
	tx_count = len(block_info.vtx)

	if tx_count >=2 : # then we have more than just a coinbase transaction in the current block
	
		print "Found it ..."
		print " "
		print "Block Number:", blockno, "	Difficulty:", block_info.difficulty
		print "Nonce: ", block_info.nNonce, "	Time: ", block_info.nTime
		print "Block Hash: "
		print bitcoin.core.b2lx(block_info.GetHash())
		print " "
		print "Transaction Details:"
  		for x in range (1, 2) :  
			thetx = vtx[x] #grab the CTransaction object 
			vin = thetx.vin #grab the CTxIn object
			vout = thetx.vout #grab the CTxOut object
		
			print "tx:",bitcoin.core.b2lx(thetx.GetHash())
			print " "
		
			if len(vin) >= 1 :
				print "Inputs: (",len(vin),")" 
				for i in range (0, len(vin)) :
					vi = vin[i]
					vip = vi.prevout
					print bitcoin.core.b2lx(vip.hash)
					## and finally it includes a signature
					print " "
				
			vov = 0
			if len(vout) >= 1 : 
				print "Outputs: (",len(vout),")"
				for o in range (0, len(vout)) :
					vo = vout[o]
					print "Value: ", bitcoin.core.str_money_value(vo.nValue)
					print "is_valid: ", vo.is_valid()
					print "scriptPubKey: "
					print bitcoin.core.b2x(vo.scriptPubKey)
					vov = vov + vo.nValue
					print " " 
				print bitcoin.core.str_money_value(5000000000), "	Total Input Value"
				print bitcoin.core.str_money_value(vov), "	Total Output Value"
				print bitcoin.core.str_money_value(5000000000-vov), "	Transaction Fees"	
				## OK we have finished
				exit()
