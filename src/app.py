from crypt import methods
from flask import Flask, make_response, redirect, request, render_template, session, url_for, flash
from flask_bootstrap import Bootstrap5

from config import config

# Routes
from routes import Image
from routes import Inicio


app = Flask(__name__)

def page_not_found(error):
    return '<h1>Página no encontrada</h1>',404

if __name__ == '__main__':
    app.config.from_object(config['development'])

    bootstrap = Bootstrap5(app)
    # Blueprints
    app.register_blueprint(Inicio.main, url_prefix=('/'))



    # Error Handlers
    app.register_error_handler(404, page_not_found)
    app.run()