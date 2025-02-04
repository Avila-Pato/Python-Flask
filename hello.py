from flask import Flask, render_template

app = Flask(__name__)


@app.route("/index")
@app.route("/")
def index():
    name = "pato"
    friends = ["pato", "pepe", "pepa", "pepito"]
    return render_template("index.html", name=name, friends=friends)


@app.route("/hello")
@app.route("/hello/<name>")
@app.route("/hello/<name>/<int:age>")
def hello_world(name=None, age=None):
    if name & age == None:
        return "<p>Hello, World!</p>"
    elif age == None:
        return f"<p>Hello, {name}!</p>"
    elif name == None:
        return f"<p>Hello, {age}!</p>"


from markupsafe import escape


@app.route("/code/<path:code>")
def code(code):
    return f"<p>{escape(code)}</p>"
