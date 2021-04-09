# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "WELCOME PROJECT-NOVA- "


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
