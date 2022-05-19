from crypt import methods
from flask import Flask, make_response, redirect, request, render_template, session, url_for, flash
from flask_login import login_required


from app import create_app
from app.form import LoginForm 

app = create_app()

template_folder = './templates'
static_folder = './static'

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

todos = imagenes[:limite]

gallery = ['./static/img/sites/photo1.jpg',
            './static/img/sites/photo2.jpg',
            './static/img/sites/photo3.jpg',
            './static/img/sites/photo4.jpg',
            './static/img/sites/photo5.jpg',
            './static/img/sites/photo6.jpg']


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
        'gallery': gallery,
        'todos': todos,
        'login_form': login_form,
        'username': username
    }

    if login_form.validate_on_submit():
        username = login_form.username.data
        session['username'] = username

        flash('Nombre de usuario registrado con exito')

        return render_template('inicio.html', **context)

    return render_template('inicio.html', **context)