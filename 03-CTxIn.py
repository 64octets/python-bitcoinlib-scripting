### Open Provenance February 2016 - https://myveryown.org
### Bitcoin Blockchain Information using python-bitcoinlib
### CTxIn & COutPoint Objects and Properties
### Donate to Open Provenance: 1opDUZQ9nsL1LJALBdV1dvqSMtcvNj9EC

## Import the modules required and setup a connection to bitcoin
import bitcoin

## Create a proxy object and connect to the bitcoin.rpc 
import bitcoin.rpc
myproxy = bitcoin.rpc.Proxy()

## Get the latest CBlock data from bitcoin rpc proxy
block_info = myproxy.getblock(myproxy.getblockhash(myproxy.getblockcount()))

## From the CBlock object we are able to get the transactions
vtx = block_info.vtx

## Print the details to the screen.
print "----------------------------------------------------------------"
print "Bitcoin CTxIn Object Information: Block Height ", myproxy.getblockcount()
print "----------------------------------------------------------------"

## We need a non coinbase transaction for this demo as coinbase transactions are no inputs.
## in this example we will show the second transaction or first non "coinbase" transaction details.

if len(vtx) > 2 :
  for x in range (1, 2) :

	## Each Transaction is a CTransaction Object
	thetx = vtx[x]

	## Now we have the object we can get info from it
	print "Is Coinbase: ", thetx.is_coinbase()
	print "nVersion: ", thetx.nVersion
	print "nLockTime: ", thetx.nLockTime
	print "TxHash: "
	print bitcoin.core.b2lx(thetx.GetHash())

	## From the CTransaction Object we get the CTxIn Objects
	vin = thetx.vin

	## There could be more than one IN so we loop
	if len(vin) >= 1 :
		for i in range (0, len(vin)) :
			## vi is a CTxIn Object
			vi = vin[i]
			print " " 
			## From this Object we can get info
			print "is_final: ", vi.is_final()
			print "nSequence : ", vi.nSequence
			## the CTxIn Object also contains one or many COutPoint Objects
			vip = vi.prevout
			print "COutPoint Hash: "
			print bitcoin.core.b2lx(vip.hash)
			print "COutPoint n: ", vip.n
			print "COutPoint is_null: ", vip.is_null()
			## and finally it includes a signature
			print "scriptSig : "
			print bitcoin.core.b2lx(vi.scriptSig)
			print '----------'
else :
	print "Sorry this block only has a coinbase transaction."
print "----------------------------------------------------------------"
print " "  
exit()
