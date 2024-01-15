from flask import Flask, render_template, request

app = Flask(__name__)
# กำหนด url แล้วดึงข้อมูล
@app.route("/login")
def login():
    return render_template("login.html")
@app.route("/register")
def Home():
    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)
