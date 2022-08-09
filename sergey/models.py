from app import db

from datetime import datetime
from sqlalchemy.sql import func

from flask_security import RoleMixin, SQLAlchemyUserDatastore, UserMixin

class UserSubmit(db.Model):
    """Таблица заполненных форм (для БД)."""
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), index = True)
    email = db.Column(db.String(120), index = True)


class Role(db.Model, RoleMixin):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    description = db.Column(db.String(255))
    permissions = db.Column(db.UnicodeText, nullable=True)
    update_datetime = db.Column(
        db.DateTime,
        nullable=False,
        server_default=func.now(),
        onupdate=datetime.utcnow,
    )

    def __hash__(self):
        return hash(self.name)


class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    fs_uniquifier = db.Column(db.String(64), unique=True, nullable=False)
    us_totp_secrets = db.Column(db.Text, nullable=True)
    us_phone_number = db.Column(db.String(128), nullable=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    username = db.Column(db.String(255), unique=True, nullable=True)
    password = db.Column(db.String(255), nullable=False)
    last_login_at = db.Column(db.DateTime)
    last_login_ip = db.Column(db.String(100))
    current_login_at = db.Column(db.DateTime())
    current_login_ip = db.Column(db.String(100))
    active = db.Column(db.Boolean())
    login_count = db.Column(db.Integer)
    confirmed_at = db.Column(db.DateTime)
    first_name = db.Column(db.String(255), nullable=True)
    last_name = db.Column(db.String(255), nullable=True)

    create_datetime = db.Column(db.DateTime, nullable=False, server_default=func.now())
    update_datetime = db.Column(
        db.DateTime,
        nullable=False,
        server_default=func.now(),
        onupdate=datetime.utcnow,
    )

    roles = db.relationship("Role", secondary="roles_users", backref=db.backref("users", lazy="dynamic"))


roles_users = db.Table(
    "roles_users",
    db.Model.metadata,
    db.Column("user_id", db.Integer, db.ForeignKey("users.id")),
    db.Column("role_id", db.Integer, db.ForeignKey("roles.id")),
)

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
