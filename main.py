from flask import Flask, render_template
app = Flask(__name__)
app.config["CACHE_TYPE"] = "null"
@app.route('/')
def index():
    return render_template('index.html')