from flask import Flask
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