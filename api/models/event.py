from django.db import models
from host import Host

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=350)
    date = models.DateTimeField()
    venue = models.CharField(max_length=450)
    banner = models.ImageField()
    host = models.ForeignKey(Host, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    
    
    def __str__(self):
        return self.name

class TicketType(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Ticket(models.Model):
    id = models.AutoField(primary_key=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='tickets')
    ticket_type = models.ForeignKey(TicketType, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_available = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"{self.ticket_type.name} - {self.event.name}"


