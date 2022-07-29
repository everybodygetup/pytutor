
from flask_wtf import FlaskForm
from wtforms import StringField,EmailField,SubmitField,TextAreaField
from wtforms.validators import DataRequired,Email


class DemoForm(FlaskForm):
    """Класс демо-формы."""
    name = StringField('Имя')
    email = EmailField(
        "Email", validators=[
            DataRequired("Email обязателен для заполнения"),
            Email("Email введён неправильно")
        ]
    )

    message = TextAreaField("Сообщение", validators=[
        DataRequired("Сообщение обязательно для заполнения")
    ])

    submit = SubmitField('Отправить сообщение')
