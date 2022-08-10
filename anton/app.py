from extensions import db
from flask import redirect, render_template, request, url_for
from flask_security import current_user, login_required, roles_required
from forms import DemoForm
from init import app
from mail import send_email
from models import UserSubmit, User, Role, user_datastore


@app.before_first_request
def init():
    db.create_all()
    user_datastore.find_or_create_role(name="admin", permissions={"admin-read", "admin-write", "user-read", "user-write", "partner-read", "partner-write"})
    user_datastore.find_or_create_role(name="monitor", permissions={"admin-read", "user-read"})
    user_datastore.find_or_create_role(name="partner", permissions={"partner-read", "partner-write"})
    user_datastore.find_or_create_role(name="user", permissions={"user-read", "user-write"})
    user_datastore.find_or_create_role(name="reader", permissions={"user-read"})
    db.session.commit()


@app.route("/", methods=["GET", "POST"])
def index():
    """Показ главной страницы."""
    page_title = "Главная"

    return render_template("index.j2", page_title=page_title, is_index=True)


@app.get("/admin")
@login_required
@roles_required('admin')
def admin():
    return render_template("admin/index.j2")


@app.get("/admin/users")
@roles_required('admin')
def admin_users():
    user_list_db = User.query.all()
    return render_template("admin/users.j2", users=user_list_db)


@app.get("/admin/user/<int:user_id>/roles")
@roles_required('admin')
def admin_user_roles(user_id):
    user_db = User.query.get_or_404(user_id)
    roles_db = Role.query.all()
    return render_template("admin/roles.j2", user=user_db, roles=roles_db)


@app.get("/admin/user/<int:user_id>/<int:role_id>/add")
@roles_required('admin')
def admin_user_role_add(user_id, role_id):
    user_db = User.query.get_or_404(user_id)
    role_db = Role.query.get_or_404(role_id)
    user_datastore.add_role_to_user(user_db, role_db)
    db.session.commit()
    return redirect(url_for('admin_user_roles', user_id=user_id))


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
