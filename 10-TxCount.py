### Open Provenance March 2016 - https://myveryown.org
### Bitcoin Blockchain Information using python-bitcoinlib
### Count of Transactions in first 10,001 Blocks
### Donate to Open Provenance: 1opDUZQ9nsL1LJALBdV1dvqSMtcvNj9EC

## In this script we search the blockchain and count the no of transactions in the first 10,001 blocks
# Hint 10,092 

## Import the modules required and setup a connection to bitcoin
import bitcoin

## Create a proxy object and connect to the bitcoin.rpc 
import bitcoin.rpc
myproxy = bitcoin.rpc.Proxy()

## Declare some variables used by our search
starting_block = 0
ending_block = 10000
total_txs = 0

print "Counting Transactions ..."

## Now search block by block until we find what we are looking for
for blockno in range (starting_block, ending_block) :
	
	block_info = myproxy.getblock(myproxy.getblockhash(blockno))
	vtx = block_info.vtx
	tx_count = len(block_info.vtx)
	total_txs = total_txs + tx_count

print " "
print "Total Transactions: ", total_txs