from services.paystack import accept_payments #import our function here
from schemas import Payments,PaystackWebhookPayload
from fastapi import FastAPI,HTTPException,status
# create an app
app = FastAPI()


@app.post("/initialize-transactions")
async def initialize_payment(payment_details:Payments):
  payment_url = accept_payments(email=payment_details.email,amount=payment_details.amount)
  if payment_url is None:
    return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Invalid request")
  return {"payment_url":payment_url}

@app.post("/paystack-webhook")
async def paystack_webhook(payload:PaystackWebhookPayload):
    if payload.event == "charge.success":
        payment_data = payload.data
        print(payment_data)
        return {"message":"Payment successful"}
    return {"message":"Payment failed"}
