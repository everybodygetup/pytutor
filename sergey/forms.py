from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email


class Feedback(FlaskForm):
    """Форма обратной связи"""

    name = StringField("Имя")
    email = EmailField(
        "Email",
        validators=[
            DataRequired("Email обязательно для заполнения"),
            Email("Email введён неправильно"),
        ],
    )
    message = TextAreaField(
        "Сообщение", validators=[DataRequired("Сообщение обязательно для заполнения")]
    )
    submit = SubmitField("Отправить сообщение")
