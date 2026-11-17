from flask import Flask
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
    
    # Blueprint HTML
    from .html import html as html_blueprint
    app.register_blueprint(html_blueprint, url_prefix='/html')
    
    # Blueprint API 
    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    # Blueprint HEALTH CHECK
    from .health import health_bp
    app.register_blueprint(health_bp)

    # Blueprint METRICAS
    from .metrics import metrics as metrics_blueprint
    app.register_blueprint(metrics_blueprint)
    
    return app