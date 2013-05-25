from __future__ import unicode_literals

from flask import Flask


app = Flask(__name__)

app.secret_key = b'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

from app import views
