from flask import Flask, render_template
from flask_assets import Environment, Bundle
import os
app = Flask(__name__)
assets = Environment(app)

css_bundle = Bundle(
    'styles/tether.min.css',
    'styles/bootstrap.min.css',
    'styles/wth.css',
    'styles/faq.css',
    'styles/landing.css',
    'styles/nav-bar.css',
    'styles/prizesproblems.css',
    'styles/sponsors.css',
    'styles/world-changing.css',
    'styles/wth-mobile.css',
    'styles/landing-mobile.css',
    'styles/nav-bar-mobile.css',
    'styles/prizesproblems-mobile.css',
filters='cssmin',output='gen/styles.css')
assets.register('css_all',css_bundle)


js_bundle = Bundle(
'scripts/jquery-3.2.1.min.js',
'scripts/tether.min.js',
'scripts/bootstrap.min.js',
'scripts/anime.min.js',
'scripts/wth.js',filters='jsmin',output='gen/scripts.js'
)
assets.register('js_all',js_bundle)
app.config['ASSETS_DEBUG'] = False
app.config['DEBUG'] = False
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def index():
    return render_template('index.html')

