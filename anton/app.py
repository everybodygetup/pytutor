from extensions import db
from flask import redirect, render_template, request
from flask_security import current_user, login_required
from forms import DemoForm
from init import app
from mail import send_email
from models import UserSubmit


@app.before_first_request
def init():
    db.create_all()


@app.route("/", methods=["GET", "POST"])
def index():
    """Показ главной страницы."""
    page_title = "Главная"

    return render_template("index.j2", page_title=page_title)


@app.route("/mail", methods=["GET", "POST"])
def test_mail():
    page_title = "Главная"
    send_email("Тестовое письмо")
    return render_template("index.j2", page_title=page_title)


@app.get("/lk")
@login_required
def lk():
    """Личный кабинет."""
    page_title = "Личный кабинет"
    email = current_user.email
    return f"Личный кабинет: {email}"


@app.route("/test")
def test():
    """Показ тестовой страницы."""
    page_title = "Тестовая страница"
    return render_template("test.j2", page_title=page_title)


@app.route("/users")
def users():
    """Вывод списка пользователей."""
    page_title = "Список пользователей, кто заполнил форму"
    user_list_db = UserSubmit.query.all()
    return render_template("users.j2", page_title=page_title, users=user_list_db)


@app.route("/thanks")
def thanks():
    """При успешной отправке формы."""
    page_title = "Спасибо за заполнение формы!"
    return render_template("thanks.j2", page_title=page_title)


@app.route("/form", methods=["GET", "POST"])
def demo_form():
    """Форма для отправки и сохранение в БД."""
    page_title = "Демо-форма"
    form = DemoForm()
    if form.validate_on_submit():
        print(
            f"Имя кто заполнил: {request.form.get('name')}, \nEmail: {request.form.get('email')}"
        )
        user_db = UserSubmit(
            name=f"{request.form.get('name')} {request.form.get('last_name')}",
            email=request.form.get("email"),
        )
        db.session.add(user_db)
        db.session.commit()

        user_list_db = UserSubmit.query.all()
        for user in user_list_db:
            print(user.id, user.name, user.email)
        return redirect("thanks")
    return render_template("test-form.j2", page_title=page_title, form=form)
