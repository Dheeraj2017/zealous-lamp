#!/usr/bin/env/pthon3  -tt

from flask import Flask,url_for,request,render_template;
from app import app;
#here below the first 'app' is the name of the file 'app.py' and second 'app' is
#the variable 'app' that is 'app=Flask(__name__)'

import redis;
#connect to redis data store

r=redis.StrictRedis(host='localhost',port=6379,db=0,charset='utf-8',decode_responses=True);

#server/

@app.route('/')

def hello():

	#alternative way to connect to redis, each command is equivalent
	#r=redis.StrictRedis();
	#r=redis.StrictRedis('localhost',6379,0);

#here below 'url_for('create')' the ('create') is the name of the function
#here below we link the first page with the '/create' by making the link

	createLink="<a href='" + url_for('create') + "'>Create a question</a>";
	return """ <html>
                      <head>
                          <title>Hello, World</title>
                      </head>
                      <body>
			  <h1>Hello this is Dheeraj !!!</h1>
                          """ + createLink + """
                      </body>
                   </html>""";


#server /create

@app.route('/create', methods=['GET', 'POST'])

def create():  

	if request.method == 'GET' :

		#send the form to user

		return render_template('CreateQuestion.html');

	elif request.method == 'POST' :

		#read the form data

		title = request.form['title'];

		question = request.form['question'];

		answer=request.form['answer'];
		
		#stores data in the data stores
		#key name will be whatever title they typed in : Question
		#e.g. music:question countries:Question
		#e.g. music:answer countries:answer

		r.set(title +':question',question)
		r.set(title +':answer',answer)

		return render_template('CreatedQuestion.html',question = question);

#here in the above line the 1st question is the new variable parameter  and the 2nd question is the above 'question = request.form['question']'

	else :

		return "<h2>Invalid request</h2>"


#server/question/<title>

@app.route('/question/<title>',methods=['GET','POST'])

#@app.route('/question/<int:title>')
#@app.route('/question/<str:title>')

def question(title):

	if request.method == 'GET':

		#send the user the form

#below code is used to grab the questions made by in the above create question.html page

		#question = 'Question here.';
		#this below code is taking value to redis datastore
		question=r.get(title+':question')
		#Read question from data store

		return render_template('AnswerQuestion.html',question = question);

	elif request.method == 'POST' :

		#User has attemped answer. Check if they are correct

		submittedAnswer = request.form['submittedAnswer'];
		
		#Read answer from data store

		#answer = 'Answer';
		#redis code to show the answer
		answer = r.get(title+':answer')

		
		if submittedAnswer == answer:

			return render_template('Correct.html');

		else:

			return render_template('Incorrect.html',answer = answer,submittedAnswer = submittedAnswer);
	else :

		return '<h2>Invalid request<h2>';


