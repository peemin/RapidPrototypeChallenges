from flask import Flask
from flask import request
from flask import render_template


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World Peemin Chen - Rapid Prototyping 2014!'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
	return render_template('hello.html', name=name)

@app.route('/challenge3/')
@app.route('/challenge3/<name>')
def challenge3(name=None):
	return render_template('challenge3.html', name=name)	

@app.route('/find', methods=['GET'])
def find():
	course = request.args['course']
	if course == 'CSCI1300':
		classroom = 'ATLAS 100'
	elif course == 'CSCI2240':
		classroom = 'ITTL 1B50'
	else:
		classroom = 'Sorry. No result for '+ course
	return 'Find the Classroom for '+course+'...'+classroom

@app.route('/notification/')
def notification():
    return 'Get Notification. To be implemented'   

if __name__ == '__main__':
	app.debug = True
	app.run()