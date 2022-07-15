from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email


class ContactForm(FlaskForm):
    name = StringField("Имя")
    email = EmailField(
        "Email", validators=[
            DataRequired("Заполните Email"),
            Email("Email введен неправильно")
        ]
    )
    message = TextAreaField("Message", validators=[DataRequired("Заполните поле")])
    submit = SubmitField("Отправить")
