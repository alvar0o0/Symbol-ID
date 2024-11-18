from flask import Flask
from config import Config
from app.extensions import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Inicializar extensiones
    db.init_app(app)
    
    # Registrar rutas
    from app.routes import main
    app.register_blueprint(main.bp)
    
    # Crear tablas
    with app.app_context():
        db.create_all()
    
    return app