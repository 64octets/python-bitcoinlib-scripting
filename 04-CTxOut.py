### Open Provenance February 2016 - https://myveryown.org
### Bitcoin Blockchain Information using python-bitcoinlib
### CTxOut Objects and Properties
### Donate to Open Provenance: 1opDUZQ9nsL1LJALBdV1dvqSMtcvNj9EC

## Import the modules required and setup a connection to bitcoin
import bitcoin

## Create a proxy object and connect to the bitcoin.rpc 
import bitcoin.rpc
myproxy = bitcoin.rpc.Proxy()

## Get the latest CBlock data from bitcoin rpc proxy
block_info = myproxy.getblock(myproxy.getblockhash(myproxy.getblockcount()))

## From the CBlock object we are able to get the transaction info
vtx = block_info.vtx

## Print the details to the screen.
print "----------------------------------------------------------------"
print "Bitcoin CTxOut Object Information: Block Height ", myproxy.getblockcount()
print "----------------------------------------------------------------"

## We need a non coinbase transaction for this demo
## we could loop all transaction with 'for x in range (0, len(vtx)) :'
## but in this example we will show the second transaction or first non "coinbase" transaction details.
 
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

	## From the CTransaction Object we get the CTxOut Objects
	vout = thetx.vout

	## There could be more than one so we loop
	if len(vout) >= 1 :
		vov = 0
		for o in range (0, len(vout)) :
			## vo is a CTxOut Object
			vo = vout[o]
			## From this Object we can get info
			print "Value: ", vo.nValue
			print "is_valid: ", vo.is_valid()
			print "COutPoint Hash :"
			print bitcoin.core.b2x(vo.GetHash())
			print "scriptPubKey: "
			print bitcoin.core.b2x(vo.scriptPubKey)
			print '--------'
			vov = vov + vo.nValue
		print " " 
		print "Total Output Value: ", vov
else :
	print "Sorry this block only has a coinbase transaction."
print "----------------------------------------------------------------"
print " "  
exit()
