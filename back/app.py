"""System module."""
from flask_cors import CORS
from flask import Flask 
import logging
# # import fonctions as fct

APP = Flask(__name__)
CORS(APP)

logging.basicConfig(level=logging.DEBUG)


@APP.route('/', methods=['GET', 'POST'])
def entry_point():
  """docstring zfzef zefzafza zvzeveza"""
  return "Hello"

@APP.route('/hello_world')
def hello_world():
  """docstring zfzef zefzafza zvzeveza"""
  return 'Hello World'


if __name__ == '__main__':
  # app.config.update(ENV="development", DEBUG=True)
  # app.run(host="0.0.0.0")
  APP.run(debug=True)
