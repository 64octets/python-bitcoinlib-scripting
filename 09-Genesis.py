### Open Provenance February 2016 - https://myveryown.org
### Bitcoin Blockchain Information using python-bitcoinlib
### The Genesis Block Message 
### Donate to Open Provenance: 1opDUZQ9nsL1LJALBdV1dvqSMtcvNj9EC

## Import the modules required and setup a connection to bitcoin
import bitcoin

## Create a proxy object and connect to the bitcoin.rpc 
import bitcoin.rpc
myproxy = bitcoin.rpc.Proxy()

## Grab the genesis block
block_info = myproxy.getblock(myproxy.getblockhash(0))

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

print vip

