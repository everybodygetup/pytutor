from flask import Flask, redirect, render_template, request, url_for

from form import Demoform

app = Flask(__name__)
app.config["SECRET_KEY"] = "0qwe"

@app.route("/", methods={'GET', 'POST'})
def index():
    user_name = 'Serik'
    form = Demoform(request.form)
    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template('index.j2', user_name=user_name, form=form)

@app.route('/thanks')
def thanks():
    page_title = 'Спасибо за заполнение формы'
    return render_template("thanks.j2", page_title=page_title)

@app.route('/test')
def test():
    return render_template("test.j2")

