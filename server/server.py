# server.py
import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__, static_folder="../app/dist",
            template_folder="../app/dist")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/hello")
def hello():
    return "Hello World!"


@app.route('/<path:path>')
def static_proxy(path):
    """ static folder serve """
    file_name = path.split('/')[-1]
    print(file_name)
    dir_name = os.path.join('../app/dist', '/'.join(path.split('/')[:-1]))
    print(dir_name)
    return send_from_directory(dir_name, file_name)


if __name__ == "__main__":
    app.run()
