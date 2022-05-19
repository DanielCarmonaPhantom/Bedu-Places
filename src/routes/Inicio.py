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

imagenes = [('./static/img/sites/beach1.jpg',6), 
            ('./static/img/sites/mountain1.jpg',3), 
            ('./static/img/sites/beach2.jpg',3),
            ('./static/img/sites/mountain2.jpg',3), 
            ('./static/img/sites/beach3.jpg',3),
            ('./static/img/sites/mountain3.jpg',3), 
            ('./static/img/sites/beach4.jpg',3),
            ('./static/img/sites/mountain4.jpg',6), 
            ('./static/img/sites/beach5.jpg',3),
            ('./static/img/sites/mountain5.jpg',3), 
            ('./static/img/sites/beach6.jpg',3),
            ('./static/img/sites/beach7.jpg',3), 
            ('./static/img/sites/beach8.jpg',6),
            ('./static/img/sites/beach1.jpg',3), 
            ('./static/img/sites/beach1.jpg',6),]
contador = 0
limite = 0

for imagen in imagenes:
    if contador <48:
        contador += imagen[1]
        limite +=1


todos = ImagenModel.get_images()

gallery = ['./static/img/sites/photo1.jpg',
            './static/img/sites/photo2.jpg',
            './static/img/sites/photo3.jpg',
            './static/img/sites/photo4.jpg',
            './static/img/sites/photo5.jpg',
            './static/img/sites/photo6.jpg']



main=Blueprint('inicio_blueprint',__name__)

@main.route('/')
def inicio():
    user_ip = request.remote_addr 
    session['user_ip'] = user_ip
    user_ip = session.get('user_ip')

    login_form = LoginForm()
    username = session.get('username')

    context = {
        'user_ip': user_ip,
        'gallery': gallery,
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