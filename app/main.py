from flask import Flask
from web3.auto import w3


app = Flask(__name__)

account_1 = '0xFa37214c234dF3479246AB5a850a11d591A93240'

@app.route("/")
def home_view():
	return "<h1>Hello World!</h1>"

	
@app.route('/test_address/<string:address>', methods=['GET'])
def test_address(address):
	return w3.isChecksumAddress(address)
	
@app.route('/bet_bear')
def bet_bear():

	nonce = web3.eth.getTransactionCount(account_1)
	
	tx = {
    'nonce': nonce,
    'to': '0x00',
    'value': web3.toWei(1, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei')
	}
	
	return json.dumps(tx)