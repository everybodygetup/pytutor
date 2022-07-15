from flask import redirect, render_template, request, url_for
"""из фласка импортируем класс(Flask), подключаем (рендрим) шаблоны из фласка."""
from forms import Feedback
from init import app, db
from models import UserSubmit

"""c помощью декоратора @app делаем зрительный образ, то что должно показывать на главной странице."""
"""GET запросы возвращают инфо браузеру, POST отправляют инфо на сервер."""
@app.route("/", methods=['GET', 'POST'])
def index():
    db.create_all()
    """В шаблоне base через url_for передал функции (index)"""
    user_name = 'Sergey'
    """Передаем в render_template -> передается из контрролера в шаблон index.html."""
    form = Feedback(request.form)
    if form.validate_on_submit():
        """print(f"Имя кто заполнил: {request.form.get('name')}, \nEmail: {request.form.get('email')}")"""
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


@app.route("/work")
def work():
    return render_template('work.html')


@app.route("/study")
def study():
    return render_template('study.html')


@app.route("/life")
def life():
    return render_template('life.html')


"""Тестовый декоратор"""
@app.route("/test")
def test():
    return render_template('test.html')
