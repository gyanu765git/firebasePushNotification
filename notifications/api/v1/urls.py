
from django.urls import path
from .views import *


urlpatterns = [
    path('send/', sendNotification.as_view(), name = 'send_notificaiton')
]