### Python-bitcoinlib Scripting Examples

In this repo you will find some basic scripts that utilise Peter Todd's python-bitcoinlib.

We have found basic examples hard to find online, so we thought we would make a few to help others to learn

First we show how to query the wallet to obtain its balance then how to send coins in 00-send.py

Second we show you how to access the following objects:

*CBlock, CTransaction, CTxIn, COutPoint and CTxOut*

Assuming you have complied and installed bitcoin, use the following commands to download and install the latest python-bitcoinlib from Peter Todds repository on Github

```
git clone https://github.com/petertodd/python-bitcoinlib
```

Then run the following commands as root to install

```
cd python-bitcoinlib
python setup.py build
python setup.py install
```

To run the scripts in this repo please use the following syntax:

``` python 00-send.py ```

If you would like to dump the output of an Object example script to a text file then use the following syntax

``` python 01-CBlock.py > 01-CBlock.txt ```

For more detailed information on python-bitcoinlib please see
https://media.readthedocs.org/pdf/python-bitcoinlib/latest/python-bitcoinlib.pdf

#### Donations & Support

Open Provenance is open source!

If you would like to donate to the Open Provenance Project our official donation address is: 1opDUZQ9nsL1LJALBdV1dvqSMtcvNj9EC

If you would like to give support with your abilities please get in touch via Twitter @OpenProvenance.
