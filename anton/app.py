from flask import flash, g, redirect, render_template, request, url_for
from flask_security import current_user, login_required, roles_required

from extensions import db
from forms import DemoForm
from init import app
from mail import send_email
from models import Role, User, UserSubmit, user_datastore


@app.before_first_request
def init():
    db.create_all()
    user_datastore.find_or_create_role(
        name="admin",
        permissions={
            "admin-read",
            "admin-write",
            "user-read",
            "user-write",
            "partner-read",
            "partner-write",
        },
    )
    user_datastore.find_or_create_role(
        name="monitor", permissions={"admin-read", "user-read"}
    )
    user_datastore.find_or_create_role(
        name="partner", permissions={"partner-read", "partner-write"}
    )
    user_datastore.find_or_create_role(
        name="user", permissions={"user-read", "user-write"}
    )
    user_datastore.find_or_create_role(name="reader", permissions={"user-read"})
    db.session.commit()


@app.route("/", methods=["GET", "POST"])
def index():
    """Показ главной страницы."""
    g.page_title = "Главная"
    return render_template("index.j2", is_index=True)


@app.get("/admin")
@login_required
@roles_required("admin")
def admin():
    """Главная страница админки."""
    g.page_title = "Админка"
    return render_template("admin/index.j2")


@app.get("/admin/users")
@roles_required("admin")
def admin_users():
    """Список всех пользователей сайта."""
    user_list_db = User.query.all()
    g.page_title = "Список пользователей"
    return render_template("admin/users.j2", users=user_list_db)


@app.get("/admin/user/<int:user_id>/roles")
@roles_required("admin")
def admin_user_roles(user_id):
    """Управление ролями конкретного пользователя."""
    user_db = User.query.get_or_404(user_id)
    roles_db = Role.query.all()
    g.page_title = f"Управление ролями для пользователя {user_db.email}"
    return render_template("admin/roles.j2", user=user_db, roles=roles_db)


@app.get("/admin/user/<int:user_id>/<int:role_id>/add")
@roles_required("admin")
def admin_user_role_add(user_id, role_id):
    """Добавление роли пользователю."""
    user_db = User.query.get_or_404(user_id)
    role_db = Role.query.get_or_404(role_id)
    user_datastore.add_role_to_user(user_db, role_db)
    db.session.commit()
    flash(
        f"Успешно добавлена роль «{role_db.name}» пользователю «{user_db.email}»",
        "success",
    )
    return redirect(url_for("admin_user_roles", user_id=user_id))


@app.get("/admin/user/<int:user_id>/<int:role_id>/remove")
@roles_required("admin")
def admin_user_role_remove(user_id, role_id):
    """Удаление роли пользователя."""
    user_db = User.query.get_or_404(user_id)
    role_db = Role.query.get_or_404(role_id)
    if role_db.name == "admin" and user_db == current_user:
        flash("Админу нельзя снять админские права самому себе", "danger")
    else:
        user_datastore.remove_role_from_user(user_db, role_db)
        db.session.commit()
        flash(
            f"Успешно удалена роль «{role_db.name}» пользователю «{user_db.email}»",
            "success",
        )
    return redirect(url_for("admin_user_roles", user_id=user_id))


@app.route("/mail", methods=["GET", "POST"])
def test_mail():
    """Тестовая отправка письма админам."""
    send_email("Тестовое письмо")
    g.page_title = "Тестовая отправка письма"
    return render_template("index.j2")


@app.get("/lk")
@login_required
def lk():
    """Личный кабинет."""
    g.page_title = "Личный кабинет"
    return render_template("lk/index.j2")


@app.route("/test")
def test():
    """Показ тестовой страницы."""
    g.page_title = "Тестовая страница"
    return render_template("test.j2")


@app.route("/users")
def users():
    """Вывод списка пользователей."""
    user_list_db = UserSubmit.query.all()
    g.page_title = f"Список пользователей, кто заполнил форму: {len(user_list_db)}"
    return render_template("users.j2", users=user_list_db)


@app.route("/thanks")
def thanks():
    """При успешной отправке формы."""
    g.page_title = "Спасибо за заполнение формы!"
    return render_template("thanks.j2")


@app.route("/form", methods=["GET", "POST"])
def demo_form():
    """Форма для отправки и сохранение в БД."""
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

        flash("Форма успешно отправлена добавлена", "success")
        return redirect("thanks")
    g.page_title = "Демо-форма"
    return render_template("test-form.j2", form=form)
