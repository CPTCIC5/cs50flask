from flask import Flask, redirect, render_template, request, session
from flask_session import Session
app = Flask(__name__)
app.config ["SESSION_PERMANENT" ] = False
app.config ["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():     
    return render_template("index.html",name=session.get('name'))

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        session['name'] == request.form.get("name")
        print('mila sessin')
        name= request.form.get(name)
        password= request.form.get(password)
        return render_template('login.html')
    
if __name__ == '__main__':
    app.run(debug=True)