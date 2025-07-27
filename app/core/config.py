import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """
    Application configuration class loading environment variables.

    Attributes:
        DEBUG (bool): Enable debug mode if True. Defaults to False.
        AUTH_KEY (str): Authentication key for securing endpoints.
        GOOGLE_MAPS_API_KEY (str): API key for Google Maps services.
        OPENAI_API_KEY (str): API key for OpenAI services.

        GOOGLE_MAPS_API_SALT (str): Salt used in Google Maps API requests.
        GOOGLE_MAPS_API_SIGNATURE (str): Signature used for Google Maps API.
        GOOGLE_MAPS_CLIENT_ID (str): Client ID for Google Maps API.
        GOOGLE_MAPS_GMP_CLIENT_SIGNALS (str): GMP client signals for Google Maps.
        GOOGLE_MAPS_SESSION_ID (str): Session ID for Google Maps API requests.
    """

    DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "yes")
    AUTH_KEY = os.getenv("AUTH_KEY", "")
    GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY", "")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

    GOOGLE_MAPS_API_SALT = os.getenv("GOOGLE_MAPS_API_SALT", "")
    GOOGLE_MAPS_API_SIGNATURE = os.getenv("GOOGLE_MAPS_API_SIGNATURE", "")
    GOOGLE_MAPS_CLIENT_ID = os.getenv("GOOGLE_MAPS_CLIENT_ID", "")
    GOOGLE_MAPS_GMP_CLIENT_SIGNALS = os.getenv("GOOGLE_MAPS_GMP_CLIENT_SIGNALS", "")
    GOOGLE_MAPS_SESSION_ID = os.getenv("GOOGLE_MAPS_SESSION_ID", "")
