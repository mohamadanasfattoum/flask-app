from flask import Flask



app = Flask(__name__)

@app.route('/') # the app path 
def home():   # the first app
    return 'Hello! this is the main page <h1>HELLO<h1>'  # the html template

@app.route('/<name>')
def user(name):
    return f'Hello {name} !'

if __name__ == '__main__':
    app.run()