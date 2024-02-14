from django.urls import path
from .views import EventView, SearchEventView

urlpatterns = [
    path('page', EventView.as_view(), name='listview'),
    path('search', SearchEventView.as_view(), name='search')
]
