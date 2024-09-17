# notifications/urls.py
from django.urls import path,include
from .views import *


urlpatterns = [
    path('', index, name = 'home_page'),
    path('api/v1/', include("notifications.api.v1.urls"))

]
