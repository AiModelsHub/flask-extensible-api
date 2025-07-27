from flasgger import Swagger

swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "Your API",
        "description": "API documentation with Swagger",
        "version": "1.0.0"
    },
    "definitions": {
        "ApiResponse": {
            "type": "object",
            "properties": {
                "message": {"type": "string"},
                "code": {"type": "integer"},
                "status": {"type": "string"},
                "data": {"type": "object"}
            }
        }
    }
}

def init_swagger(app):
    """
    Initialize and attach Swagger UI to the Flask application.

    Args:
        app (Flask): The Flask application instance.

    Returns:
        Swagger: An instance of the Swagger documentation initialized with the app.
    """
    return Swagger(app, template=swagger_template)
