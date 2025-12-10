import requests
from config import settings


PAYSTACK_SECRET_KEY = settings.PAYSTACK_SECRET_KEY


def accept_payments(email:str,amount:str):
    url="https://api.paystack.co/transaction/initialize"
    headers = {
        "Authorization":f"Bearer {PAYSTACK_SECRET_KEY}",
    }
    data = {
        "email":email,
        "amount":amount
    }
    
    try:
        response = requests.post(url,headers=headers,data=data)
        response.raise_for_status()
        return response.json()["data"]["authorization_url"]
    except requests.exceptions.HTTPError as e:
        return None