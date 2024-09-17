import os
from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse

# Write views from here.....
############################ service worker #######################
"""
Note:
service worker file should be accessible at this url http://localhost:8001/firebase-messaging-sw.js
for this firebase-messaging-sw.js should be kept where manage.py file located
"""    
def serviceWorker(request):
    filepath = os.path.join('firebase-messaging-sw.js')
    return FileResponse(open(filepath, 'rb'), content_type='application/javascript')

def serviceWorker2(request):
    data='importScripts("https://www.gstatic.com/firebasejs/8.8.0/firebase-app.js");' \
         'importScripts("https://www.gstatic.com/firebasejs/8.8.0/firebase-messaging.js")"); ' \
         'var firebaseConfig = {' \
         '        apiKey: "AIzaSyA5QXTBDrkkt6RKDiEJlz2xVjq_YAL7Jww",' \
         '        authDomain: "ludo-27977.firebaseapp.com",' \
         '        databaseURL: "https://ludo-27977-default-rtdb.firebaseio.com",' \
         '        projectId: "ludo-27977",' \
         '        storageBucket: "ludo-27977.appspot.com",' \
         '        messagingSenderId: "773216686826",' \
         '        appId: "1:773216686826:web:2c86813e6a5a284914bd93",' \
         '        measurementId: "G-D84371JPYJ"' \
         ' };' \
         'firebase.initializeApp(firebaseConfig);' \
         'const messaging=firebase.messaging();' \
         'messaging.setBackgroundMessageHandler(function (payload) {' \
         '    console.log(payload);' \
         '    const notification=JSON.parse(payload);' \
         '    const notificationOption={' \
         '        body:notification.body,' \
         '        icon:notification.icon' \
         '    };' \
         '    return self.registration.showNotification(payload.notification.title,notificationOption);' \
         '});'

    return HttpResponse(data,content_type="text/javascript")


def index(request):
    return render(request , 'base.html')


