from django.contrib import admin
from .models.event import Event, TicketType, Ticket
from .models.host import Host, BankDetail

class TicketInline(admin.TabularInline):
    model = Ticket

class EventAdmin(admin.ModelAdmin):
    inlines = [
        TicketInline,
    ]
    list_display = ('name', 'date', 'venue', 'host')
    search_fields = ('name', 'venue')
    list_filter = ('host',)

class TicketTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class HostAdmin(admin.ModelAdmin):
    list_display = ('user', 'event_count',)
    search_fields = ('user__username',)
    list_filter = ('event_count',)

class BankDetailAdmin(admin.ModelAdmin):
    list_display = ('acc_name', 'bank', 'acc_number', 'email',)
    search_fields = ('acc_name', 'bank', 'email',)

admin.site.register(Event, EventAdmin)
admin.site.register(TicketType, TicketTypeAdmin)
admin.site.register(Host, HostAdmin)
admin.site.register(BankDetail, BankDetailAdmin)
