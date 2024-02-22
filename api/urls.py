from django.urls import path
from .endpoints.event import EventView, CreateEvent
from .endpoints.auth import RegisterUser, LoginUser, BuyTicket
from .endpoints.host import Host, CreateTicketType, HostAccountDetail
# SearchEventView


urlpatterns = [
    path('event-list', EventView.as_view(), name='listview'),
    # path('search', SearchEventView.as_view(), name='search'),
    path('login', LoginUser.as_view(), name='login'),
    # path('host', Host.as_view(), name='host'),
    path('ce', CreateEvent.as_view(), name='create-event'),
    path('ctt', CreateTicketType.as_view(), name='create-ticket-type'),
    path('had', HostAccountDetail.as_view(), name='host-account-detail'),
    path('bt', BuyTicket.as_view(), name='buy-ticket'),
    path('register', RegisterUser.as_view(), name='register')
]

{
    "username": "testuserg",
    "email": "test@user.com",
    "password": "testpass"
}

{
    "email": "test@user.com",
    "password": "testpass"
}
