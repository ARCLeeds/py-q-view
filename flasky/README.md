#PyQView

This repository contains the source code for PyQview

####Requirements:
	
	python3.4
	
	
	Flask==0.10.1
	Flask-Bootstrap==3.0.3.1
	Flask-Cors==2.1.2
	Flask-Login==0.3.2
	Flask-Mail==0.9.0
	Flask-Migrate==1.1.0
	Flask-Moment==0.2.1
	Flask-Script==0.6.6
	Flask-SQLAlchemy==1.0
	Flask-WTF==0.9.4
	Werkzeug==0.10.4
	Jinja2==2.7.1
	Mako==0.9.1
	MarkupSafe==0.18
	SQLAlchemy==0.9.9
	WTForms==1.0.5
	Werkzeug==0.10.4
	alembic==0.6.2
	blinker==1.3
	itsdangerous==0.23
	pycrypto==2.6.1
	paramiko==2.0.2
	Babel==2.3.3
	
It is not essential but a virtual environment can be created natively with python 3.4 to install these packages in. Python 3.4 must be used because paramiko requires C libraries that are compiled specifically for python 3.4.

To use the email functionality and arc connectivity environment variables need to be set 

PYNAME = your arc username 

PYWORD = your arc password

MAIL\_USERNAME = your email

MAIL\_PASSWORD = your password

To run the server move into the flasky directory and run `python3.4 manage.py runserver` this will run the server on the local host in debug mode. It is essential that debug mode is turned off if this server is listening on a public port. 

##Tutorials on flask that I have used for this project.
 
Resource containing lots of tutorials

https://www.fullstackpython.com/flask.html

Miguel grinbergs flask blog

http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

W3s bootstrap tutorial

http://www.w3schools.com/bootstrap/default.asp

And also a book by Miguel Grinberg entitled Flask Web Development
