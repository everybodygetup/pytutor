from flask import render_template, request, redirect, url_for  # Импорт из модуля класс Flask, render - передаем шаблон
from forms import DemoForm
from init import app, db

from models import UserSubmit




@app.route("/", methods = ['GET', 'POST'])
def index():  # В шаблоне base через url_for передал функции (index/test)
    user_name = 'Artem'  # Передаем в render_template -> передается из контрролера в шаблон index.html
    form = DemoForm(request.form)
    if form.validate_on_submit():
        print(f"Имя кто заполнил: {request.form.get('name')}, \nEmail: {request.form.get('email')}")
        user_db = UserSubmit(
            name=f"{request.form.get('name')} {request.form.get('last_name')}",
            email=request.form.get('email')
        )
        db.session.add(user_db)
        db.session.commit()

        user_list_db = UserSubmit.query.all()
        for user in user_list_db:
            print(user.id, user.name, user.email)
        return redirect(url_for('index'))
    return render_template('index.html',user_name=user_name,form=form)



@app.before_first_request
def create_tables():
    db.create_all()


@app.route('/test')
def test():
    return render_template('test.html')


@app.route('/services/<service_name>')
def services(service_name):
    return render_template('service.html', service_name=service_name)


