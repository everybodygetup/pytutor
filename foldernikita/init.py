import os

from flask import Flask

from config import config
from extensions import babel, mail, db, migrate, security, executor
from mail import SecMailUtil
from models import user_datastore


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config.from_object(config[os.getenv("FLASK_ENV", "production")])
app.config.update(
    SQLALCHEMY_DATABASE_URI=f"sqlite:///{os.path.join(basedir, 'app.db')}",
)
babel.init_app(app)
mail.init_app(app)
executor.init_app(app)
db.init_app(app)
migrate.init_app(app, db)
# app, user_datastore, mail_util_cls=SecMailUtil
security.init_app(app, user_datastore, mail_util_cls=SecMailUtil)
