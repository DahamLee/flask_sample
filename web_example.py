from sqlite3 import dbapi2 as sqlite3
from contextlib import closing
from hashlib import md5
import time
from datetime import datetime
from flask import Flask, request, session, url_for, redirect, render_template, g, flash, abort
from werkzeug.security import generate_password_hash, check_password_hash
import sys

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def web_page():
    python_version = sys.version
    return render_template('page_template.html', version=python_version)


if __name__ == '__main__':
    app.run()
