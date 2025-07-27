from flask import Flask
from app.routes.burst_routes import burst_bp

def register_routes(app: Flask):
    app.register_blueprint(burst_bp, url_prefix="/api")
