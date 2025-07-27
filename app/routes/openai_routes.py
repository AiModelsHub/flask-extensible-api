from flask import Blueprint, request, jsonify
from app.services import openai_service
from app.models.response import ApiResponse

openai_bp = Blueprint("openai", __name__)

@openai_bp.route("/generate-text", methods=["POST"])
def generate_text():
    """
    Generate text using OpenAI API.
    ---
    tags:
      - OpenAI
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            prompt:
              type: string
              example: "Write a short poem about the ocean."
            model:
              type: string
              example: "gpt-4"
            max_tokens:
              type: integer
              example: 150
    responses:
      200:
        description: Generated text successfully
        schema:
          $ref: '#/definitions/ApiResponse'
      500:
        description: Error while generating text
        schema:
          $ref: '#/definitions/ApiResponse'
    """
    data = request.get_json()
    prompt = data.get("prompt")
    model = data.get("model", "gpt-4")
    max_tokens = data.get("max_tokens", 200)

    result = openai_service.generate_text(prompt, model, max_tokens)

    resp = ApiResponse(
        message="Text generated successfully" if "output" in result else "Failed to generate text",
        code=200 if "output" in result else 500,
        status="ok" if "output" in result else "error",
        data=result
    )
    return jsonify(resp.dict()), resp.code
