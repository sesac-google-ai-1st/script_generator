from flask import Flask, render_template, url_for
from flask import current_app, send_from_directory
import os

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
