from django.contrib.auth.models import User
from django.db import models

class Payment(models.Model):
    class TRANSACTION_STATUS(models.TextChoices):
        SUCCESSFUL = "SUCCESSFUL", "Successful"
        PENDING = "PENDING", "Pending"
        FAILED = "FAILED", "Failed"
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, name=None)
    description = models.TextField(null=True, blank=True)
    amount = models.FloatField(default="0.00")
    status = models.CharField(
        max_length=50,
        choices=TRANSACTION_STATUS.choices,
        default=TRANSACTION_STATUS.PENDING,
    )
    ref =  models.CharField(max_length=100)
    time = models.DateTimeField()
    
    def __str__(self):
        return f"{self.user.username}'s Transaction"

    class Meta:
        ordering = ["-created_at"]