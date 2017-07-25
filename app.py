from flask import Flask
from flask import render_template
import logging
import os
import json

from datetime import datetime

app = Flask(__name__)
HOME_DIR = os.getcwd()
PAGE_DIR = os.path.join(HOME_DIR, 'pages')
DEFAULT_PAGE="Home"

def load_pages(folder=PAGE_DIR):
    for filename in os.listdir(folder):
        path = os.path.join(folder, filename)
        if os.path.isdir(path):
            load_pages(path)
            continue
        content = None
        with open(os.path.join(folder, filename), 'r') as f:
            content = f.read()
        attr = path[len(PAGE_DIR)+1:]
        logging.info("Adding: %s", attr)
        setattr(app, attr, content)


@app.route("/<path:pg>")
@app.route("/")
def load_page(pg=None):
    if not pg:
        pg = DEFAULT_PAGE
    if hasattr(app, pg):
        return getattr(app, pg)
    else:
        logging.warn("Cannot find: %s", pg)
        return getattr(app, DEFAULT_PAGE)



load_pages()


if __name__ == "__main__":
    print "Started Squeal..."
    app.run()
    print "Squeal done."
