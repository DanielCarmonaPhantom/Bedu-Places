from crypt import methods
from flask import Flask, make_response, redirect, request, render_template, session, url_for, flash
from flask_bootstrap import Bootstrap4

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = 'SUPER SECRETO'
bootstrap = Bootstrap4(app)

template_folder = './templates'
static_folder = './static'

todos = ['Comprar Cafe', 'Enviar solicitud de compra', 'Todo M3']

class LoginForm(FlaskForm):
    username = StringField('Nombre de Usuario', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Enviar')

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error = error)

@app.route('/')
def index():
    user_ip = request.remote_addr 
    response = make_response(redirect('/inicio'))
    session['user_ip'] = user_ip
    return response


@app.route('/inicio', methods=['GET', 'POST'])
def inicio():
    user_ip = session.get('user_ip')
    login_form = LoginForm()

    username = session.get('username')

    context = {
        'user_ip': user_ip,
        'todos': todos,
        'login_form': login_form,
        'username': username
    }

    if login_form.validate_on_submit():
        username = login_form.username.data
        session['username'] = username

        flash('Nombre de usuario registrado con exito')

        return redirect(url_for('inicio'))

    return render_template('inicio.html', **context)