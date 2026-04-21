import os

from flask import redirect, render_template, Flask
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = os.urandom(24)


class DoubleForm(FlaskForm):
    id_astro = StringField('Id астронавта', validators=[DataRequired()])
    pass_astro = PasswordField('Пароль астронавта', validators=[DataRequired()])
    id_cap = StringField('Id капитана', validators=[DataRequired()])
    pass_cap = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = DoubleForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Аварийный доступ', form=form)


@app.route('/success')
def success():
    return 'Успешно войдено'


if __name__ == '__main__':
    app.run(port=8080)
