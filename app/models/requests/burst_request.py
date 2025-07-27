from pydantic import BaseModel, Field

class BurstRequest(BaseModel):
    total_requests: int = Field(default=100, ge=1)
    workers: int = Field(default=10, ge=1)
    stream: bool = Field(default=False)