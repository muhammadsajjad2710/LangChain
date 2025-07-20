from pydantic import BaseModel
from typing import Optional, Dict

class TransferRequest(BaseModel):
    engagementId: str
    details: Dict

class HandoffRequest(BaseModel):
    shared_id: str

class TokenData(BaseModel):
    access_token: str
    token_type: str
