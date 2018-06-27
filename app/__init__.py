from flask import Flask,request,jsonify
from logging.config import dictConfig
from flask_sqlalchemy import SQLAlchemy
from py2neo import Graph
from .model.entity.neo.site import Site
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

url = 'http://localhost:7687'
username = 'neo4j'
password = 'password'

graph = Graph(url + '/db/data/', username=username, password=password)

site = Site(11,'322323232')
# graph.push(site)
