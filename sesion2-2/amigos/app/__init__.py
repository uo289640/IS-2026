from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import app_config

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)
    
    migrate = Migrate(app, db)
    
    from app import models
    from app.models import Amigo  # Lo importamos aquí para usarlo en todas las rutas

    # Mostrar la tabla de amigos
    @app.route('/amigos')
    def tabla_amigos():
        amigos = Amigo.query.all()
        return render_template('tabla_amigos.html', amigos=amigos)

    # Mostrar el formulario vacío para crear un amigo
    @app.route('/new_amigo')
    def new_amigo():
        return render_template('formulario.html', amigo=None)

    # Mostrar el formulario relleno para editar un amigo existente
    @app.route('/edit_amigo/<int:id>')
    def edit_amigo(id):
        amigo = Amigo.query.get(id)
        return render_template('formulario.html', amigo=amigo)

    # Borrar un amigo y volver a la tabla
    @app.route('/delete_amigo/<int:id>')
    def delete_amigo(id):
        amigo = Amigo.query.get(id)
        if amigo:
            db.session.delete(amigo)
            db.session.commit()
        return redirect('/amigos')

    # Recibir los datos del formulario 
    @app.route('/save_amigo', methods=['POST'])
    def save_amigo():
        id_amigo = request.form.get('id')
        name = request.form.get('name')
        lati = request.form.get('lati')
        longi = request.form.get('longi')

        if id_amigo:  # Si hay ID, actualizamos el amigo existente
            amigo = Amigo.query.get(id_amigo)
            amigo.name = name
            amigo.lati = lati
            amigo.longi = longi
        else:  # Si no hay ID, creamos uno nuevo
            amigo = Amigo(name=name, lati=lati, longi=longi)
            db.session.add(amigo)
        
        db.session.commit()
        return redirect('/amigos')

    return app
