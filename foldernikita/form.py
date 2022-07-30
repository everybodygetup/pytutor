from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email


class ContactForm(FlaskForm):
    name = StringField("Имя")
    email = EmailField(
        "Email", validators=[
            DataRequired("Заполните Email"),
            Email("Email введен неправильно")
        ]
    )
    message = TextAreaField("Сообщение", validators=[DataRequired("Заполните поле")])
    submit = SubmitField("Отправить")

class ContactsForm(FlaskForm):
    adress = StringField("Адрес", validators=[DataRequired("Заполните поле")])
    phone = StringField("Телефон", validators=[DataRequired("Заполните поле")])
    telegram = StringField("Телеграм", validators=[DataRequired("Заполните поле")])
    instagram = StringField("Инстаграм", validators=[DataRequired("Заполните поле")])
    submit = SubmitField("Заменить данные на сайте")

class RatingForm(FlaskForm):
    rating = SelectField("Ваша оценка",
        validators=[DataRequired()],
        choices=[("1"),("2"),("3"),("4"),("5")]
    )
    comments= StringField("Ваши замечания")
    submit = SubmitField("Оставить оценку")
