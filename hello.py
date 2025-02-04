from flask import Flask  # type: ignore

app = Flask(__name__)


@app.route("/index")
def index():
    return "<p>Pagina de inicio</p>"


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
