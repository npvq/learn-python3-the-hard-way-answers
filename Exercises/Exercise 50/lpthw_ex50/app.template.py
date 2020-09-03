# Simplest piece of code for a Flask application.
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    greeting = "World"
    return f"Hello, {greeting}"


if __name__ == "__main__":
    app.run()
