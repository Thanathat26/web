from flask import Flask, request,render_template, redirect,session
from flask_sqlalchemy import SQLAlchemy
import bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
app.secret_key = 'secret_key'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

    def __init__(self,email,password,name):
        self.name = name
        self.email = email
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    def check_password(self,password):
        return bcrypt.checkpw(password.encode('utf-8'),self.password.encode('utf-8'))

with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        name = request.form['username']
        email = request.form['email']
        password = request.form['password']

        new_user = User(name=name,email=email,password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect('/login')



    return render_template('register.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        name = request.form['username']
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            session['email'] = user.email
            return redirect('/Home')
        else:
            return render_template('login.html',error='Invalid user')

    return render_template('login.html')
# กำหนด url แล้วดึงข้อมูล
#login

#registr

#home
@app.route("/Home")
def Home():
    return render_template("home.html")
#room1
@app.route("/room1")
def room1():
    return render_template("room1.html")
#room2
@app.route("/room2")
def room2():
    return render_template("room2.html")
#room3
@app.route("/room3")
def room3():
    return render_template("room3.html")
#room4
@app.route("/room4")
def room4():
    return render_template("room4.html")
#room5
@app.route("/room5")
def room5():
    return render_template("room5.html")    
#room6
@app.route("/room6")
def room6():
    return render_template("room6.html") 

@app.route("/about")
def about():
    return render_template("about.html") 

@app.route("/contact")
def contact():
    return render_template("contact.html") 

#run
if __name__ == "__main__":
    app.run(debug=True)
