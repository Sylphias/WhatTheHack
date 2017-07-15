"""
This script runs the FlaskWebProject application using a development server.
"""

from os import environ
from flask import Flask, render_template

if __name__ == '__main__':

    app = Flask(__name__)
	app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
	@app.route('/')
	def index():
	    return render_template('index.html')
