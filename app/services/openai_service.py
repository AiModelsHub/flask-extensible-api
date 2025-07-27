from openai import OpenAI
from typing import Optional, Dict
from app.core.config import Config

class OpenAIService:
    """
    Service for interacting with OpenAI API.

    Uses the OpenAI Python SDK and reads the API key from Config.
    """

    def __init__(self):
        """
        Initialize OpenAI client using API key from Config.
        """
        if not Config.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY is not set in the configuration.")
        self.client = OpenAI(api_key=Config.OPENAI_API_KEY)

    def generate_text(self, prompt: str, model: str = "gpt-4", max_tokens: int = 200) -> Dict[str, str]:
        """
        Generate text using OpenAI's language model.

        Args:
            prompt (str): The input text or prompt.
            model (str): Model name (e.g., "gpt-4"). Defaults to "gpt-4".
            max_tokens (int): Maximum tokens to generate. Defaults to 200.

        Returns:
            Dict[str, str]: A dictionary with the generated text or an error.
        """

        try:
            response = self.client.responses.create(
            model=model,
            input=prompt,
            max_output_tokens=max_tokens
        )
            return {"output": response.output_text}
        except Exception as e:
            return {"error": str(e)}

    def chat_completion(self, messages: list, model: str = "gpt-4") -> Dict[str, str]:
        """
        Create a chat completion using OpenAI API.

        Args:
            messages (list): List of dicts representing conversation messages.
                             Example: [{"role": "user", "content": "Hello!"}]
            model (str): Model name (e.g., "gpt-4"). Defaults to "gpt-4".

        Returns:
            Dict[str, str]: A dictionary with the assistant's reply or an error.
        """
        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=messages
            )
            return {"output": response.choices[0].message["content"]}
        except Exception as e:
            return {"error": str(e)}
