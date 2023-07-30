from pydantic import BaseModel

class SpamFilterRequest(BaseModel):
    text: str