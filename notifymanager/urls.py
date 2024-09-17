from django.contrib import admin
from django.urls import path,include
from notifications.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('notifications/', include("notifications.urls")),
    path('firebase-messaging-sw.js', serviceWorker, name='service-worker'),
    # path('firebase-messaging-sw.js', serviceWorker2, name='show_firebase_js'),
]
