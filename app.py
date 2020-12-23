from flask import Flask, request, render_template
from flask_mail import Mail, Message


app = Flask(__name__)

	
@app.route('/',methods=['POST','GET'])
def index():
	return render_template('MyMailProjForm.html')


@app.route('/login', methods=['POST','GET'])
def login():
	#print(list(request.form['re'].split(",")),"***************************")
	app.config['MAIL_SERVER'] = 'smtp.gmail.com' 
	app.config['MAIL_PORT'] = 465
	app.config['MAIL_USERNAME'] = request.form['se']
	app.config['MAIL_PASSWORD'] = request.form['pa']
	app.config['MAIL_USE_TLS'] = False
	app.config['MAIL_USE_SSL'] = True
	mail = Mail(app)

	msg = Message(request.form['su'], sender= request.form['se'], recipients=list(request.form['re'].split(",")))
	msg.body = request.form['bo']
	mail.send(msg)
	return "Mail Sent"

if __name__ == '__main__':
	app.run(debug=True)

