from flask import Flask, render_template, request
#ps -a --> kill -9 pid
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/greet", methods=["POST"])
def greet():
    return render_template("greet.html", name=request.form.get("name","world"))


