import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()
secret_key = os.environ.get("PAYSTACK_PIR_KEY")

class Paystack:
    def __init__(self, email, amount, secret_key):
        self.email = email
        self.amount = amount
        self.secret_key = secret_key

    def initialize_transaction(self):
        url = "https://api.paystack.co/transaction/initialize"
        headers = {
            "Authorization": "Bearer " + self.secret_key,
            "Content-Type": "application/json"
        }
        data = {
            "email": self.email,
            "amount": str(self.amount)  # Amount should be a string in Python, same as in Node.js
        }

        response = requests.post(url, headers=headers, data=json.dumps(data))
        return response.json()
