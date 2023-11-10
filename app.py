from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
	return render_template('index.html')


@app.route('/cc_payment')
def cc_payment():  # put application's code here
	return render_template('single_payment.html')


@app.route('/charge', methods=['POST', 'GET'])
def charge():
	if request.method == "POST":
		payment_key = request.form["payment_key"]
		
	
	return render_template('charge_result.html')


if __name__ == '__main__':
	app.run()
