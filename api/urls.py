from django.urls import path
from .endpoints.event import EventView, CreateEvent, SearchEventView
from .endpoints.auth import RegisterUser, LoginUser, BuyTicket
from .endpoints.host import HostView, CreateTicketType, HostAccountDetail
from .paystack.main import Checkout


urlpatterns = [
    path('host', HostView.as_view(), name='host'),
    path('event-list', EventView.as_view(), name='listview'),
    path('search', SearchEventView.as_view(), name='search'),
    path('login', LoginUser.as_view(), name='login'),
    path('pay', Checkout.as_view(), name='pay'),
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

{
    "email": "test@user.com",
    "amount": "200",
    "quantity": "2"
}

{
    "email": "test@user.com",
    "amount": 200,
    "quantity": 2
}