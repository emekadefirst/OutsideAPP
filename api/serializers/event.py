from rest_framework import serializers
from ..models.event import Event, Ticket, TicketType

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

    def create(self, validated_data):
        event = Event.objects.create(
            name=validated_data['name'],
            date=validated_data['date'],
            venue=validated_data['venue'],
            banner=validated_data['banner'],
            host=validated_data['host']
        )
        return event
    
class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'

    def create(self, validated_data):
        ticket = Ticket.objects.create(
            event=validated_data['event'],
            ticket_type=validated_data['ticket_type'],
            price=validated_data['price'],
        )
        return ticket
    
class TicketTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketType
        fields = '__all__'
        
        def create(self, validated_data):
            tickettype = TicketType.objects.create(
                name=validated_data['name'],
            )
            return tickettype