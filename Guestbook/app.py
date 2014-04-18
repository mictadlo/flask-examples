# -*- coding: utf-8 -*-

from flask import Flask
from .controllers import *

app = Flask('__name__')

app.config['COUCHDB_SERVER'] = 'http://localhost:5984/'
app.config['COUCHDB_DATABASE'] = 'example-guestbook'
app.config['example-guestbook'] = 'set this to something secret'
app.config['SECRET_KEY'] = 'random'

# application setup
app = Flask(__name__)
app.config.from_object(__name__)

manager.setup(app)


if __name__ == '__main__':
    app.run(debug=True)