### Open Provenance February 2016 - https://myveryown.org
### Simple sending of bitcoins using python-bitcoinlib
### Donate to Open Provenance: 1opDUZQ9nsL1LJALBdV1dvqSMtcvNj9EC

## This script is intentionally simple so as to work on both 
## testnet and mainnet without modification.

## Import the modules required
import bitcoin
import bitcoin.rpc

## Create a proxy object and connect to the bitcoin.rpc 
myproxy = bitcoin.rpc.Proxy()

## Obtain the walltet balance
bal = myproxy.getbalance()

## Display this to the user
print "Your balance is :", bal, " satoshis"

## Request address to send coins to from the user
address = raw_input("Please enter the address to send to: ")
if len(address) == 0 :
    print "No address supplied, have a nice day!"
else :
    ## Request amount to send from the user
    satoshis = raw_input("Please enter the number of satoshis to send: ")
    if len(satoshis) == 0 :
        print "We can not send zero satoshis, have a nice day!"
    else :
        ## Send the amount specified to the address supplied
        myproxy.sendtoaddress(address, satoshis)
        print "Coins have been sent, have a nice day!"
exit()
