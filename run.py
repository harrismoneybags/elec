from flask import Flask, render_template

#make an instance 
app = Flask(__name__)

# make a decorater
@app.route('/')

#def index():
	#return "<h1> Hello world </h1>"


@app.route('/')

def index():
	return render_template("index.html")


@app.route('/services')

def services():
	return render_template("services.html")


@app.route('/about')

def about():
	return render_template("about.html")


@app.route('/projects')

def projects():
	return render_template("projects.html")

#costem error pages

#invalied url
@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"),404

#internal server error
@app.errorhandler(500)
def page_not_found(e):
	return render_template("500.html"),500