import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

THREADS_PER_PAGE = 2

CSRF_ENABLED = False

SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/postgres'
SQLALCHEMY_POOL_RECYCLE = 3600
SQLALCHEMY_POOL_SIZE = 10
SQLALCHEMY_TRACK_MODIFICATIONS = False