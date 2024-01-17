from flask import Flask,request,render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy


app= Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db= SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(30))
    sport = db.Column(db.String(30))

    def __repr__(self):
        return self.name
    

SPORTS = ["Basketball", "Soccer", "Ultimate Frisbee"]
REGISTRANTS= {}

@app.route('/11',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        print(name)
        return redirect(url_for('greet',name=name))
    return render_template('index.html')


@app.route('/greet-<string:name>')
def greet(name):
    return render_template('greet.html',name=name)

@app.route('/')
def home():
    return render_template('home.html',sport=SPORTS)

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        name=request.form.get('name')
        sport=request.form.get('sport')
        print(name,sport)
        db.session.add(name,sport)
        db.session.commit()
    return render_template('home.html',sport=SPORTS)

@app.route('/display')
def registerants():
    return render_template("registrants.html", registrants=REGISTRANTS)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)