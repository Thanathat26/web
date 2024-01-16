from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from flask import redirect
from wtforms import Form, StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_login import (
    LoginManager,
    login_required,
    logout_user,
    login_user,
    UserMixin,
    current_user,
)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'thisissecretkey'
db = SQLAlchemy(app)
#ไม่เอาgit คนอื่นทั้งดุ้น
class user(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),nullable=False)
    password = db.Column(db.String(80),nullable=False)
class RegisterForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Register')
    def validate_username(self, username):
        existing_user_username = User.query.filter_by(
            username=username.data).first()
        if existing_user_username:
            raise ValidationError(
                'That username already exists. Please choose a different one.')
    
class LoginForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Login')
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
@app.route("/home")
def Home():
    return render_template("home.html")
#run
if __name__ == "__main__":
    app.run(debug=True)
