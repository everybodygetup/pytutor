from flask import redirect, render_template, request, url_for
from mail import send_email
from flask_security import login_required, roles_required

# Это импортируем из созданных нами
from extensions import (
    db,
)  # изменили обращение к db, теперь из папки расширений (extensions)
from forms import Feedback
from init import app
from models import UserSubmit, User, Role, user_datastore


@app.before_first_request
def init():
    """Чтобы обращение было один раз (если хотим вводить данные постоянно - before_request)."""
    db.create_all()
    # user_datastore.create_role(name='admin', permissions={'admin-write', 'admin-read'})
    # user_datastore.create_role(name='user', permissions={'user-write', 'user-read'})
    # db.session.commit()


@app.get("/admin")
@login_required
@roles_required("admin")
def admin():
    """Делаем личный кабинет."""
    return render_template("admin/index.j2")


@app.get("/admin/users")
@roles_required("admin")
def admin_users():
    """Показ всех пользователей."""
    user_list_db = User.query.all()
    return render_template("admin/users.j2", users=user_list_db)


@app.get("/admin/user/<int:user_id>/roles")
@roles_required("admin")
def admin_user_roles(user_id):
    """Показываем роли для конкретного пользователя."""
    user_db = User.query.get_or_404(user_id)
    roles_db = Role.query.all()
    return render_template("admin/roles.j2", user=user_db, roles=roles_db)


@app.get("/admin/user/<int:user_id>/<int:role_id>/add")
@roles_required("admin")
def admin_user_role_add(user_id, role_id):
    """Добавление роли пользователю."""
    user_db = User.query.get_or_404(user_id)
    role_db = Role.query.get_or_404(role_id)
    user_datastore.add_role_to_user(user_db, role_db)
    db.session.commit()
    return redirect(url_for("admin_user_roles", user_id=user_id))


@app.route("/users")
def users():
    """Вывод списка пользователей, кто заполнил форму."""
    page_title = "Список пользователей, кто заполнил форму"
    user_list_db = UserSubmit.query.all()
    return render_template("users.j2", page_title=page_title, users=user_list_db)


@app.route("/work")
def work():
    """Страница работы."""
    page_title = "Работа"
    return render_template("work.j2", page_title=page_title)


@app.route("/study")
def study():
    """Страница учёбы."""
    page_title = "Учёба"
    return render_template("study.j2", page_title=page_title)


@app.route("/life")
def life():
    """Страница про жизнь."""
    page_title = "Жизнь"
    return render_template("life.j2", page_title=page_title)


@app.route("/", methods=["GET", "POST"])
def index():
    """В шаблоне base через url_for передал функции (index).

    С помощью декоратора @app делаем зрительный образ, то что должно показывать на главной странице.
    GET запросы возвращают инфо браузеру, POST отправляют инфо на сервер.
    """
    page_title = "Главная"
    form = Feedback(request.form)
    if form.validate_on_submit():
        user_db = UserSubmit(
            name=f"{request.form.get('name')} {request.form.get('last_name')}",
            email=request.form.get("email"),
        )
        db.session.add(user_db)
        db.session.commit()
        return redirect(url_for("index"))
    # Передаем в render_template -> передается из контрролера в шаблон index.j2.
    return render_template("index.j2", page_title=page_title, form=form, index=True)


@app.route("/mail", methods=["GET", "POST"])
def test_mail():
    """Тестовый mail."""
    page_title = "Главная"
    send_email("Тестовое письмо")
    return render_template("index.j2", page_title=page_title)
