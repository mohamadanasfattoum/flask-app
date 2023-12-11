from flask import Flask, redirect, url_for , render_template, request
# redirect zuumleiten von url zu andern


app = Flask(__name__)

@app.route('/') # the app path 
def home():   # the first app
    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET']) 
def login ():
    if request.method == 'POST': # request اداة لحمل المعلومات وارجاعها لتستخدم في المكتبة 
        user= request.form['nm']
        return redirect(url_for('user', usr=user)) # wenn wir zu def user gehen, usr = User und user= bringt die data von template mit post über request
    else:
        return render_template ('login.html')
@app.route('/<usr>')
def user (usr):
    return f'<h1>{usr}</h1>'

# @app.route('/<name>')
# def user(name):
#     return f'Hello {name} !'


# @app.route('/admin')
# def admin():
#     return redirect(url_for('user', name='Admin!'))



if __name__ == '__main__':
    app.run(debug=True)  # debug=True to keep the srver run