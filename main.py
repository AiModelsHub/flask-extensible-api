from flask import Flask
from app.services.swagger_service import init_swagger
from app.routes.burst_routes import burst_bp
from app.routes.openai_routes import openai_bp
from app.routes.health_routes import health_bp
def create_app():
    app = Flask(__name__)
    app.config.from_object("app.core.config.Config")

    init_swagger(app)

    app.register_blueprint(burst_bp, url_prefix="/api")
    app.register_blueprint(openai_bp, url_prefix="/api")
    app.register_blueprint(health_bp, url_prefix="/api")
    return app

app = create_app()