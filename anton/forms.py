from flask_wtf import FlaskForm
from wtforms import EmailField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email


class DemoForm(FlaskForm):
    """Класс демо-формы."""

    name = StringField("Имя")
    last_name = StringField("Фамилия")
    email = EmailField(
        "Email",
        validators=[
            DataRequired("Email обязателен для заполнения"),
            Email("Email введён неправильно"),
        ],
    )
    text = TextAreaField(
        "Сообщение", validators=[DataRequired("Сообщение обязательно для заполнения")]
    )
    submit = SubmitField("Отправить")
