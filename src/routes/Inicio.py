from flask import Blueprint, jsonify, make_response,request, session, flash, redirect, url_for, render_template
from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Nombre de Usuario', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Enviar')

# Models
from models.ImageModels import ImagenModel


main=Blueprint('inicio_blueprint',__name__)

@main.route('/', methods=['GET', 'POST'])
def inicio():

    imagenes = ImagenModel.get_images()
    orden = [6,3,3,3,3,3,3,6,3,3,3,3,6,3,6]
    todos = []
    for i in range(len(imagenes)):        
        todos.append(imagenes[len(imagenes) -1 - i])

    for i in range(len(todos[:13])):
        todos[i]['position'] = orden[i] 




    user_ip = request.remote_addr 
    session['user_ip'] = user_ip
    user_ip = session.get('user_ip')

    login_form = LoginForm()
    username = session.get('username')

    gallery = []

    for i in range(len(imagenes)):
        if imagenes[len(imagenes) -1 - i]['usuario'] == username:
            gallery.append(imagenes[len(imagenes) -1 - i])

    context = {
        'user_ip': user_ip,
        'gallery': gallery[:6],
        'todos': todos[:13],
        'login_form': login_form,
        'username': username
    }
    if login_form.validate_on_submit():
        username = login_form.username.data
        session['username'] = username

        flash('Nombre de usuario registrado con exito')

        return render_template('inicio.html', **context)

    return render_template('inicio.html', **context)