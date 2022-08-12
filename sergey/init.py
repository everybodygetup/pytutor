from concurrent.futures import Executor
import os

from flask import Flask

from config import config
from extensions import db, migrate, security, babel, executor, mail
from mail import SecMailUtil
from models import user_datastore

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config.from_object(config[os.getenv("FLASK_ENV", "production")])
babel.init_app(app)
executor.init_app(app)
mail.init_app(app)
"""Добавляем базу данных и механизм миграции."""
db.init_app(app)
migrate.init_app(app, db)
security.init_app(app, user_datastore, mail_util_cls=SecMailUtil)  # добавили хранилище данных пользователей
