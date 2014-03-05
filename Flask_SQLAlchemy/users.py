from flask import Flask
from flask import render_template
from challenge3 import db
from challenge3 import User 

app = Flask(__name__)

@app.route("/users")
def users():
    userlist= User.query.all()
    return render_template('users.html', users = userlist)

if __name__ == '__main__':
	app.debug = True
	app.run()