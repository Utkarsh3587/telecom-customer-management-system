from django.urls import path
from subscribers.views import SubscriberCreateListView, SubscriberDetailView

app_name = 'subscriber'

urlpatterns = [
    path('subscribers/', SubscriberCreateListView.as_view()),
    path('subscribers/(?P<pk>[0-9]+)/', SubscriberDetailView.as_view()),   
]
