from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class Demoform(FlaskForm):
    name = StringField('Имя')
    email = EmailField(
            'Email', validators=[DataRequired('Email обязательно для заполнения')]
    )
    message = TextAreaField('Сообщение')
    submit = SubmitField('Отправить сообщение')
