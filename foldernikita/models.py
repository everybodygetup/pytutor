from app import db


class UserSubmit(db.Model):
    """Таблица заявок с формы обратной связи."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    email = db.Column(db.String(128), index=True)
    message = db.Column(db.String(264), index=True)
