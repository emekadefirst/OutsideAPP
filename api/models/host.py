from django.contrib.auth.models import User
from django.db import models

"""Host withdrawal details"""
class BankDetail(models.Model):
    id = models.AutoField(primary_key=True)
    bank = models.CharField(max_length=50, default="Paystack")
    acc_number = models.IntegerField()
    acc_name = models.CharField(max_length=100, mull=True)
    email = models.CharField(max_length=150, mull=True)
    
    def __str__(self):
        return self.acc_name
    

class Host(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    event_count = models.IntegerField(default=0)
    bank_details = models.OneToOneField(BankDetail, on_delete=models.CASCADE)  

    def __str__(self):
        return self.user.username
