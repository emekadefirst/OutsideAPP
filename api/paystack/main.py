import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()
secret_key = os.environ.get("PAYSTACK_PIR_KEY")

class Paystack:
    def __init__(self, email, amount, secret_key):
        self.email = email
        self.amount = amount * 100
        self.secret_key = secret_key
        self.ref_id = None  # Initialize ref_id to None

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
        if response.status_code == 200:
            self.ref_id = response.json()['data']['reference']
        return response.json()

    def payment_status(self):
        if not self.ref_id:
            print("Error: Reference not found")
            return None
        
        url = f'https://api.paystack.co/transaction/verify/{self.ref_id}'

        headers = {
            'Authorization': f'Bearer {self.secret_key}'
        }
        response = requests.get(url, headers=headers)

        # Check for request success
        if response.status_code == 200:
            return response.json()
        else:
            # Handle errors gracefully
            print("Error:", response.text)
            return None
