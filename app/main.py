from flask import Flask
from web3.auto import w3


app = Flask(__name__)

@app.route("/")
def home_view():
	return "<h1>Hello World!</h1>"

	
@app.route('/test_address/<string:address>', methods=['GET'])
def test_address(address):
	return w3.isChecksumAddress(address)
