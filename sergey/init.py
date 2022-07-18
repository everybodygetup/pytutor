import os

from flask import Flask

from config import config
from extensions import db, migrate, security
from models import user_datastore

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config.from_object(config[os.getenv("FLASK_ENV", "production")])
app.config.update(
    SQLALCHEMY_DATABASE_URI=f"sqlite:///{os.path.join(basedir, 'app.db')}",
)
    #SECRET_KEY="gfhjkm",
    #SQLALCHEMY_DATABASE_URI=f"sqlite:///{os.path.join(basedir, 'app.db')}",
    #SQLALCHEMY_TRACK_MODIFICATIONS=False
"""Добавляем базу данных и механизм миграции."""
db.init_app(app)
migrate.init_app(app, db)
security.init_app(app, user_datastore)  # добавили хранилище данных пользователей
