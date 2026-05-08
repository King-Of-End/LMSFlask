from flask import Flask, render_template, redirect
from flask_login import LoginManager, login_user, login_required, logout_user
from flask_wtf import FlaskForm
from sqlalchemy import select
from wtforms import EmailField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

from data.db_session import create_session, global_init
from models import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)

class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')

@login_manager.user_loader
def load_user(user_id):
    db_sess = create_session()
    return db_sess.get(User, user_id)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = create_session()
        user_select = select(User).where(User.email == form.email.data)
        user = db_sess.execute(user_select).scalar()
        print(user.check_password(form.password.data))
        print(form.password.data)
        print(user.hashed_password)
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)

if __name__ == '__main__':
    global_init('db/users_new.db')
    app.run()

