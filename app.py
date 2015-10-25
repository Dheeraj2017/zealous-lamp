from flask import Flask

app=Flask(__name__)
'''
@app.route("/")
def hello():
	return """<html>
		      <head>
			<title>Hello, World</title>
		      </head>
		      <body>
			<h1>Hello , dheeraj!!</h1>
		      </body>
		  </html>""";

@app.route('/create')
def create():	
	return "<h2>this is the create page!</h2>";
'''

#Import all of our routes from routes.
from routes import *;

#launching the server
if (__name__ == "__main__"):
	import os
	HOST=os.environ.get('SERVER_HOST','localhost')
	try:
	      PORT=int(os.environ.get('SERVER_PORT',5999))
	except ValueError:
	      PORT=5999
	app.run(HOST,PORT)
	#app.run(port=5999)
