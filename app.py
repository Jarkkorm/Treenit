from flask import Flask
from os import getenv
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")
Bootstrap(app)

import routes
