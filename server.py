from flask import Flask, json

from web3.auto import w3

api = Flask(__name__)

@api.route('/getTest/<string:address>', methods=['GET'])
def deposit_address(address):
	result = w3.isChecksumAddress(address)
	return result
	
if __name__ == '__main__':
	api.run()