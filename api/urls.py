from django.urls import path
from .views import EventView, SearchEventView, RegisterUser, LoginUser, Host, CreateEvent, CreateTicketType, HostAccountDetail, BuyTicket


urlpattern = [
    path('event-list', EventView.as_view(), name='listview'),
    path('search', SearchEventView.as_view(), name='search'),
    path('login', LoginUser.as_view(), name='login'),
    path('register', RegisterUser.as_view(), name='register')
]

{
    "username": "testuser",
    "email": "test@user.com",
    "password": "testpass"
}

{
    "email": "test@user.com",
    "password": "testpass"
}
