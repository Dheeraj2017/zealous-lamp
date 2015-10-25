#do not touch below 2 code otherwise error 
from flask import Flask

app = Flask(__name__)
#here 'app' is the varible 


#make the WSGI interface available at the top level so wfastcgi can get it.
#wsgi_app=app.wsgi_app

#server /
@app.route("/")

#our code 
def hello():
	return "Hello World!"
#here in the return we can type the complete html code want to run 

if (__name__ == "__main__"):

#app.run() this can also be used but defaults it assign to '127.0.0.1:5000'
#for assigning the port we can use this which is gven below
	app.run(port = 5999)
