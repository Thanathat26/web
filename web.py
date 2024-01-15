from flask import Flask, render_template, request

app = Flask(__name__)
# กำหนด url แล้วดึงข้อมูล
@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        form = request.form['msg']
        print("Message: %s" % (form))
    return render_template("login.html")

@app.route("/Home")
def Home():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
