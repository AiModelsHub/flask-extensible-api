from flask import Flask
from app.services.swagger_service import init_swagger
from app.routes.burst_routes import burst_bp
from app.routes.openai_routes import openai_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.core.config.Config")

    init_swagger(app)

    app.register_blueprint(burst_bp, url_prefix="/api")
    app.register_blueprint(openai_bp, url_prefix="/api")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
