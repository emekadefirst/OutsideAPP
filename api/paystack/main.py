import enum
import os
import requests
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
publickey = os.environ.get("PAYSTACK_PUB_KEY")
secretkey = os.environ.get("PAYSTACK_PIR_KEY")
RECIEVE_ENDPOINT = os.environ.get("RECIEVE_ENDPOINT")
VERIFY_ENDPOINT = os.environ.get("VERIFY_ENDPOINT")

class PaystackEvents(enum.Enum):

    SUCCESS = "charge.success"
    FAILED = ""
    
class Paystack:
    """Paystack platform implementation. """
    
    def __init__(self, secret_key, public_key):
        self.secret_key = secret_key
        self.public_key = public_key
        
        self.headers = {"Authorization": "Bearer %s" % self.secret_key}
        
    def initate_payment(self, email, amount):
        payload = {"email": email, "amount":amount}
        
        response = requests.post(
            url=RECIEVE_ENDPOINT,
            data=payload,
            headers=self.headers,
        )
        return response.json()