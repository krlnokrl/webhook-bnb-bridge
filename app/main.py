from flask import Flask, json

from web3.auto import w3

app = Flask(__name__)

@app.route('/getTest/<string:address>', methods=['GET'])
def deposit_address(address):
	result = w3.isChecksumAddress(address)
	return result
	
@app.route('/')
def index():
  return 'Testing...'
if __name__ == '__main__':
	api.run()