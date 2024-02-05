from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from flask import redirect
from wtforms import Form, StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError,DataRequired,Email
from flask_login import (
    LoginManager,
    login_required,
    logout_user,
    login_user,
    UserMixin,
    current_user,
)
from flask_mysqldb import MySQL
app = Flask(__name__)
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'mydatabase'
app.secret_key = 'your_secret_key_here'

mysql = MySQL(app)
class RegisterForm(FlaskForm):
    name = StringField("Name",validators=[DataRequired()])
    email = StringField("Email",validators=[DataRequired(), Email()])
    password = PasswordField("Password",validators=[DataRequired()])
    submit = SubmitField("Register")

    def validate_email(self,field):
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM users where email=%s",(field.data,))
        user = cursor.fetchone()
        cursor.close()
        if user:
            raise ValidationError('Email Already Taken')

class LoginForm(FlaskForm):
    email = StringField("Email",validators=[DataRequired(), Email()])
    password = PasswordField("Password",validators=[DataRequired()])
    submit = SubmitField("Login")
# กำหนด url แล้วดึงข้อมูล
#login
@app.route("/login",methods=['GET','POST'])
def login():
    form = LoginForm()
    return render_template("login.html")
#registr
@app.route("/register")
def register():
    form = RegisterForm()
    return render_template("register.html")
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
def concact():
    return render_template("concact.html") 

#run
if __name__ == "__main__":
    app.run(debug=True)
