from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hellow World!'

@app.route('/test')
def test():
    return 'Test complete'

@app.route('/tests/')
def tests():
    return 'The tests where are they'

with app.test_request_context():
    print(url_for('tests'))