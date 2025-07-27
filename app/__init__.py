from flask import Flask
from app.core.extensions import db, migrate, cache, login_manager

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.core.config.Config")
    db.init_app(app)
    migrate.init_app(app, db)
    cache.init_app(app)
    login_manager.init_app(app)
    return app