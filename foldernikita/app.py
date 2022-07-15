import os

from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from form import ContactForm

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import UserSubmit

@app.route("/", methods=['GET', 'POST'])
def index():
    form = ContactForm()
    if form.validate_on_submit():
        print(f"Name: {request.form.get('name')}, \nEmail: {request.form.get('email')}, \nMessage: {request.form.get('message')}")
        user_db = UserSubmit(
            name = request.form.get('name'),
            email = request.form.get('email'),
            message = request.form.get('message')
        )
        db.session.add(user_db)
        db.session.commit()
        user_list_db = UserSubmit.query.all()
        for user in user_list_db:
            print(user.id, user.name, user.email, user.message)
        return redirect(url_for('index'))
    return render_template("index.j2", form=form)



@app.route('/test')
def test():
    return render_template("test.j2")


@app.route('/elements')
def elements():
    return render_template("elements.j2")


@app.route('/users')
def users():
    user_list_db = UserSubmit.query.all()
    return render_template("users.j2", users=user_list_db)
