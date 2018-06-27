from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from logging.config import dictConfig

import logging


dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)

app.config.from_object('config.settings')
app.config.from_envvar('FLASK_ENV',silent=True)

logger = logging.getLogger('FlaskLogger')
logger.addHandler(logging.handlers.TimedRotatingFileHandler('flask.log', when="d", interval=1, backupCount=5))

db = SQLAlchemy(app)
db.create_all()
db.session.commit()

