# Creating Forms
# A Simple Form
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/hello')
def index():
    name = request.args.get('name', 'Nobody')
    greet = request.args.get('greet', 'Hello')

    if name and greet:
        greeting = f"{greet}, {name}"
    else:
        greeting = "Hello, World!"

    return render_template("index_old.html", greeting=greeting)


if __name__ == "__main__":
    app.run()
