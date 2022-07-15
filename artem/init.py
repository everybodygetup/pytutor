import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config["SECRET_KEY"] = "ghbdtn"
# Расширение Flask-SQLAlchemy принимает местоположение базы данных приложения из переменной конфигурации SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # (Откл) должна сигнализировать приложению каждый раз, когда в базе данных должно быть внесено изменение
db = SQLAlchemy(app)  # Сделали экземпляры класса db и migrate
migrate = Migrate(app, db)
