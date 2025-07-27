from pydantic import BaseModel, Field
from typing import Optional, Any

class ApiResponse(BaseModel):
    """
    Standard API response model for consistent HTTP responses.

    Attributes:
        message (str): Response message describing the result. Defaults to "Success".
        code (int): Numeric response code (e.g., HTTP status code). Defaults to 200.
        status (str): Status string such as "ok" or "error". Defaults to "ok".
        data (Optional[Any]): Optional payload containing response data. Defaults to None.
    """

    message: str = Field(default="Success", description="Response message")
    code: int = Field(default=200, description="Response code")
    status: str = Field(default="ok", description="Response status")
    data: Optional[Any] = Field(default=None, description="Payload data")
