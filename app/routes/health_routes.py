from flask import Blueprint, jsonify

health_bp = Blueprint("health", __name__)

@health_bp.route("/health", methods=["GET"])
def health_check():
    """
    Health Check Endpoint
    ---
    tags:
      - Health
    responses:
      200:
        description: Application is healthy
        schema:
          type: object
          properties:
            status:
              type: string
              example: "ok"
            uptime_seconds:
              type: integer
              description: Seconds since app started
    """
    # Optionally add uptime or other info
    return jsonify({
        "status": "ok"
    }), 200
