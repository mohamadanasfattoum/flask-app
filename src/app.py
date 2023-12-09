from flask import Flask, redirect, url_for , render_template
# redirect zuumleiten von url zu andern


app = Flask(__name__)

@app.route('/<name>') # the app path 
def home(name):   # the first app
    return render_template('index.html', content=name, r=2)

# @app.route('/<name>')
# def user(name):
#     return f'Hello {name} !'


# @app.route('/admin')
# def admin():
#     return redirect(url_for('user', name='Admin!'))



if __name__ == '__main__':
    app.run()