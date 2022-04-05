from crypt import methods
from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello, world!\n'


@app.route('/<name>', methods=['GET'])
def hello_name(name):
    return f'Hello, {name}!\n'


@app.route('/download/', methods=['GET'])
def download_meteorite_data():
    return 

# the next statement should usually appear at the bottom of a flask app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')