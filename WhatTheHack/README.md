# What The Hack
This web application was built with flask, html5, css and simple javascript with jquery.

## Installation
### Installation of python
You can download python at the following website
https://www.python.org/downloads/windows/

### Installing flask
Flask will be our microframework that will serve as the backend of this application.
A full guide can be found here http://flask.pocoo.org/docs/0.12/installation/

`pip install flask flask-assets cssmin`

If you have issues installing flask, feel free to use codepen to do your code first then send me a link and I will do the integration into the whole application.

### Git commands
Remember the basic git commands that I went through with y'all. We will each be working on our own branch and I will be doing the merging between branches.

## Running the application
Once you have installed and done the necessary setup for the applications, you can run the following commands to start the flask server and visit you page at localhost:5000 (<--- 5000 indicates the port number, you will be able to see what port the application is running on when you start the sever.)

You will need to run the following 
```
export FLASK_APP=main.py
export FLASK_DEBUG=1
flask run
 * Running on http://127.0.0.1:5000/
 ```
The `FLASK_DEBUG=1` makes the server auto-restart when you make changes.

## Compression and minification of assets
This application uses [flask-assets](https://flask-assets.readthedocs.io/en/latest/) to perform asset bundling and minification. 
