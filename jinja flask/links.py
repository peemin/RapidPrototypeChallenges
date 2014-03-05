from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/home")
def template_test():
    rand_list= ['Google', 'Twitter', 'Wikipedia']
    rand_string = ['http://google.com', 'http://twitter.com', 'http://wikipedia.org']
    link_lists =[{'name':'Google', 'link': 'http://google.com'}, 
                 {'name':'Twitter','link':'http://twitter.com'},
                 {'name':'Wikipedia','link':'http://wikipedia.org'}]
    return render_template('links.html',
    links=link_lists)


if __name__ == '__main__':
	app.debug = True
	app.run()


