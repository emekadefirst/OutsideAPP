from django.contrib.auth.models import User
from django.db import models
from api.models.event import Ticket




class Payment(models.Model):
    class TRANSACTION_STATUS(models.TextChoices):
        SUCCESSFUL = "SUCCESSFUL", "Successful"
        PENDING = "PENDING", "Pending"
        FAILED = "FAILED", "Failed"
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, name=None)
    email = models.EmailField(max_length=100, null=True, blank=True)
    amount = models.FloatField(default="0.00")
    status = models.CharField(max_length=50, choices=TRANSACTION_STATUS.choices, default=TRANSACTION_STATUS.PENDING)
    reference =  models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)  
    
    def __str__(self):
        return f"{self.user.username}'s Transaction"

    class Meta:
        ordering = ["-time"]  # Ordering by the 'time' field in descending order

class PaymentDetail(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, name=None)
    quantity = models.IntegerField(default=0)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, name=None)
    status = models.ForeignKey(Payment, on_delete=models.CASCADE, name=None)
    
    
    def __str__(self):
        return f"{self.user.username}'s Payment Details"

    class Meta:
        ordering = ["-time"]
