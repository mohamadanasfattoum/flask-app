from flask import Flask, redirect, url_for , render_template
# redirect zuumleiten von url zu andern


app = Flask(__name__)

@app.route('/') # the app path 
def home():   # the first app
    return 'Hello! this is the main page <h1>HELLO</h1>'  # the html template

# @app.route('/<name>')
# def user(name):
#     return f'Hello {name} !'


# @app.route('/admin')
# def admin():
#     return redirect(url_for('user', name='Admin!'))



if __name__ == '__main__':
    app.run()