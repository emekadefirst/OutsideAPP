from django.contrib import admin
from .models.event import Event, TicketType, Ticket
from .models.host import Host, BankDetail
from .models.transaction import Payment

class TicketInline(admin.TabularInline):
    model = Ticket
    
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'email', 'amount', 'status', 'time', 'reference')

class EventAdmin(admin.ModelAdmin):
    inlines = [
        TicketInline,
    ]
    list_display = ('id', 'name', 'date', 'venue', 'host')
    search_fields = ('name', 'venue')
    list_filter = ('host',)

class TicketTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class HostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'event_count', 'first_name', 'middle_name', 'last_name', 'address')
    search_fields = ('user__username',)
    list_filter = ('event_count',)

class BankDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'acc_name', 'bank', 'acc_number', 'email',)
    search_fields = ('acc_name', 'bank', 'email',)

admin.site.register(Event, EventAdmin)
admin.site.register(TicketType, TicketTypeAdmin)
admin.site.register(Host, HostAdmin)
admin.site.register(BankDetail, BankDetailAdmin)
admin.site.register(Payment, PaymentAdmin)
