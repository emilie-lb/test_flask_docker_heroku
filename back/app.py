"""System module."""
from flask_cors import CORS
from flask import Flask 
import logging
# # import fonctions as fct

app = Flask(__name__)
# CORS(app)

#logging.basicConfig(level=logging.DEBUG)


@app.route('/', methods=['GET', 'POST'])
def entry_point():
  """docstring zfzef zefzafza zvzeveza"""
  return "Hello"

@app.route('/hello_world')
def hello_world():
  """docstring zfzef zefzafza zvzeveza"""
  return 'Hello World'


# if __name__ == '__main__':
#   # app.config.update(ENV="development", DEBUG=True)
#   # app.run(host="0.0.0.0")
#   app.run(debug=True)
