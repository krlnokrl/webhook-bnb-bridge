from flask import Flask
from web3 import Web3
import json

import utils

#account details
account_1 = '0x9F8cCdaFCc39F3c7D6EBf637c9151673CBc36b88'
private_key = b"\xb2\\}\xb3\x1f\xee\xd9\x12''\xbf\t9\xdcv\x9a\x96VK-\xe4\xc4rm\x03[6\xec\xf1\xe5\xb3d"


app = Flask(__name__)

#provider
web3 = Web3(Web3.HTTPProvider('https://data-seed-prebsc-1-s1.binance.org:8545'))

@app.route("/")
def home_view():
	return "Home of the API"


@app.route('/currentEpoch/')
def current_epoch():

	contract = web3.eth.contract(address=PREDICTION_CONTRACT, abi=PREDICTION_ABI)
	
	currentEpoch = contract.functions.currentEpoch().call()
	
	return str(currentEpoch)


@app.route('/betBear/<string:value>', methods=['GET'])
def bet_bear(value):

	nonce = web3.eth.getTransactionCount(account_1)
	

	contract = web3.eth.contract(address=PREDICTION_CONTRACT, abi=PREDICTION_ABI)
	
	currentEpoch = contract.functions.currentEpoch().call()
	
	bet_txn = contract.functions.betBear(currentEpoch).buildTransaction(
	{
	 'value': web3.toWei(value, 'ether'),
     'chainId': 53,
	 'gas': 70000,
     'gasPrice': web3.toWei('50', 'gwei'),
     'nonce': nonce}
	 )
	 
	signed_txn = web3.eth.account.sign_transaction(bet_txn, private_key=private_key)

	return str(signed_txn)


@app.route('/betBull/<string:value>', methods=['GET'])
def bet_bull(value):

	nonce = web3.eth.getTransactionCount(account_1)
	
	contract = web3.eth.contract(address=PREDICTION_CONTRACT, abi=PREDICTION_ABI)
	
	currentEpoch = contract.functions.currentEpoch().call()
	
	bet_txn = contract.functions.betBull(currentEpoch).buildTransaction(
	{
	 'value': web3.toWei(value, 'ether'),
     'chainId': 53,
	 'gas': 70000,
     'gasPrice': web3.toWei('50', 'gwei'),
     'nonce': nonce}
	 )
	 
	signed_txn = web3.eth.account.sign_transaction(bet_txn, private_key=private_key)

	return str(signed_txn)