from pydantic import BaseModel,EmailStr

class Payments(BaseModel):
  email: EmailStr
  amount: str

class PaystackWebhookPayload(BaseModel):
    event: str
    data: dict