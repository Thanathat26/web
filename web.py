from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import (
    LoginManager,
    login_required,
    logout_user,
    login_user,
    UserMixin,
    current_user,
)

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'thisissecretkey'

class user(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),nullable=False)
    password = db.Column(db.String(20),nullable=False)
# กำหนด url แล้วดึงข้อมูล
#login
@app.route("/login")
def login():
    return render_template("login.html")
#registr
@app.route("/register")
def Home():
    return render_template("register.html")
#home
@app.route("/home")
def Home():
    return render_template("home.html")
#
if __name__ == "__main__":
    app.run(debug=True)
