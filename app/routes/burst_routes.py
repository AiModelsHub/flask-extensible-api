from flask import Blueprint, request, Response, stream_with_context, jsonify
from app.services import run_burst_service
from app.models.requests.burst_request import BurstRequest
from app.models.response import ApiResponse
from pydantic import ValidationError
import json

burst_bp = Blueprint("burst", __name__)

@burst_bp.route("/run-burst", methods=["POST"])
def run_burst():
    """
    Run Burst Requests with Streaming Progress
    ---
    tags:
      - Burst
    consumes:
      - application/json
    produces:
      - text/event-stream
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            total_requests:
              type: integer
              default: 100
              description: Total number of requests to send
            workers:
              type: integer
              default: 10
              description: Number of concurrent workers
            stream:
              type: boolean
              default: false
              description: Stream progress events (true) or wait and return full result (false)
    responses:
      200:
        description: Streaming progress or final burst result
        content:
          text/event-stream:
            schema:
              type: string
          application/json:
            schema:
              $ref: '#/definitions/ApiResponse'
      400:
        description: Invalid request
        schema:
          $ref: '#/definitions/ApiResponse'
    """
    try:
        req = BurstRequest.parse_obj(request.get_json())
    except ValidationError as e:
        error_resp = ApiResponse(
            message="Invalid request data",
            code=400,
            status="error",
            data=e.errors()
        )
        return jsonify(error_resp.dict()), 400

    if hasattr(req, "stream") and req.stream:
        def generate_progress():
            for update in run_burst_service(req.total_requests, req.workers, stream=False):
                yield f"data: {json.dumps(update)}\n\n"
        return Response(stream_with_context(generate_progress()), mimetype='text/event-stream')

    else:
        result = run_burst_service(req.total_requests, req.workers, stream=False)
        resp = ApiResponse(
            message="Burst completed",
            code=200,
            status="ok",
            data=result
        )
        return jsonify(resp.dict()), 200
