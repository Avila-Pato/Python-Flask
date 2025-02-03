from flask import Flask  # type: ignore

app = Flask(__name__)


@app.route("/index")
def index():
    return "<p>Pagina de inicio</p>"


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
