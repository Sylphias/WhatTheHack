from flask import Flask, render_template
from flask_assets import Environment, Bundle
app = Flask(__name__)
assets = Environment(app)

css_bundle = Bundle(
    'styles/tether.min.css',
    'styles/bootstrap.min.css',
    'styles/wth.css',
    'styles/faq.css',
    'styles/landing-mobile.css',
    'styles/landing.css',
    'styles/loader.css',
    'styles/nav-bar-mobile.css',
    'styles/nav-bar.css',
    'styles/prizesproblems-mobile.css',
    'styles/prizesproblems.css',
    'styles/schedule.css',
    'styles/sponsors.css',
    'styles/workshops-mobile.css',
    'styles/workshops.css',
    'styles/world-changing.css',
    'styles/wth-mobile.css',
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

@app.template_filter('autoversion')
def autoversion_filter(filename):
  # determining fullpath might be project specific
  fullpath = os.path.join('assets/', filename[1:])
  try:
      timestamp = str(os.path.getmtime(fullpath))
  except OSError:
      return filename
  newfilename = "{0}?v={1}".format(filename, timestamp)
  return newfilename
  
@app.route('/')
def index():
    return render_template('index.html')
