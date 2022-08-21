from flask import render_template, redirect, request,url_for

from flask_security import current_user, login_required, roles_required
from mail import send_email
from init import app
from extensions import db
from forms import DemoForm
from models import UserSubmit, User, Role, user_datastore




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


@app.get("/admin") # делаем личный кабинет
@login_required
# @roles_required('admin')
def admin():
    return render_template("admin/index.html")

@app.get("/admin/users")
# @roles_required('admin')
def admin_users():
    """Показ всех пользователей."""
    user_list_db = User.query.all()
    return render_template("admin/users.html", users=user_list_db)

@app.get("/admin/user/<int:user_id>/roles")
# @roles_required('admin')
def admin_user_roles(user_id):
    """Показываем роли для конкретного пользователя."""
    user_db = User.query.get_or_404(user_id)
    roles_db = Role.query.all()
    return render_template("admin/roles.html", user=user_db, roles=roles_db)

@app.get("/admin/user/<int:user_id>/<int:role_id>/add")
# @roles_required('admin')
def admin_user_role_add(user_id, role_id):
    """Добавление роли пользователю."""
    user_db = User.query.get_or_404(user_id)
    role_db = Role.query.get_or_404(role_id)
    user_datastore.add_role_to_user(user_db, role_db)
    db.session.commit()
    return redirect(url_for('admin_user_roles', user_id=user_id))

@app.get("/lk")
@login_required
def lk():
    """Личный кабинет."""
    page_title = "Личный кабинет"
    email = current_user.email
    return f"Личный кабинет: {email}"


@app.route("/mail", methods=["GET", "POST"])
def test_mail():
    page_title = "Главная"
    send_email("Тестовое письмо")
    return render_template("index.html", page_title=page_title)


@app.route("/users")
def users():
    """Вывод списка пользователей."""
    page_title = "Список пользователей, кто заполнил форму"
    user_list_db = UserSubmit.query.all()
    return render_template("users.html", page_title=page_title, users=user_list_db)



@app.route('/test')
def test():
    return render_template('test.html')

@app.route("/about")
def about():
    page_title = 'Обо мне'
    return render_template('about.html', page_title=page_title)

@app.route("/price")
def price():
    page_title = 'Цены'
    return render_template('price.html', page_title=page_title)


@app.route('/services/<service_name>')
def services(service_name):
    return render_template('service.html', service_name=service_name)


