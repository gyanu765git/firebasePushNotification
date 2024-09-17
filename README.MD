# firebase push notification implementation in django project .............


###### Server(Backend) side config ################

1. Download the "firebase-adminsdk.json" file from: 
    a. Open the Firebase console (https://console.firebase.google.com/). 
    b. Click on the project you have created. 
    c. Click on the "settings icon" and then click on "Project settings." 
    d. Go to the "Service Accounts" tab, then under the Firebase Admin SDK section, select "Python" and  \
    click "Generate new private key."

2. Include the "firebase-adminsdk.json" file in your project and install firebase_admin: 
     "pip install firebase_admin"

3. Configure your project settings by pasting the following code into your settings.py file:

        import firebase_admin
        from firebase_admin import credentials

        firebase_creds_path = '/home/gyanu/myproject/firebase-adminsdk.json'  # copy the firebase-adminsdk.json file path
        cred = credentials.Certificate(firebase_creds_path)
        firebase_admin.initialize_app(cred)

4. Now you can create and send messages through an API in your views as shown below:

        from firebase_admin import messaging
        from rest_framework.views import APIView
        from rest_framework.response import Response
        from rest_framework import status

        class sendNotification(APIView):
            @staticmethod
            def post(request):
                notification = {
                    "title": "New Message",
                    "body": "Hey there, this is your notification..."
                }
                data = {
                    "message": "hey there, my name is gyanu chauhan....",
                }
                token = "cYWeXD9LQGBEGC6lPkD3LM:APA91bGDUuioCn53T3sLFXB3OPuNPw_tUviUYS5Wu0O1wMdSrXkUtid9HwVyh0Q4pxUHzZNg8P35sbnavOAu3JWz32__pB19i2sL0zz1kb5n3Ptuix87SCCWiXlDE8tniMEIp3uZV76kjl"
                
                message = messaging.Message(
                    notification=messaging.Notification(
                        title=notification['title'],
                        body=notification['body'],
                    ),
                    data=data, 
                    token=token,
                )
                try:
                    messaging.send(message)
                    print("Notification sent successfully")
                    return Response({"success": True, "message": "Notification sent successfully", "data": []},
                                    status=status.HTTP_200_OK)
                except Exception as e:
                    return Response({"success": False, "message": str(e), "data": []},
                                    status=status.HTTP_500_INTERNAL_SERVER_ERROR)



###### Client side config ################

1. Create a firebase-messaging-sw.js file with project's firebase-messaging-sw.js file code and place \
   it in the same directory as manage.py. You can copy the firebaseConfig from:
        a. Open the Firebase console (https://console.firebase.google.com/). 
        b. Click on the project you have created. 
        c. Click on the "settings icon" and then click on "Project settings." 
        d. select "General" tab scroll down in "SDK setup and configuration" section and copy the firebaeConfig

2. Create a method(view) in your app's views.py file and include the endpoint in your project's urls.py file. \
   (Note: Do not include the endpoint in your app's urls.py file.)    
    
    # views.py
        import os
        from django.http import FileResponse
        def serviceWorker(request):
            filepath = os.path.join('firebase-messaging-sw.js')
            return FileResponse(open(filepath, 'rb'), content_type='application/javascript')   

    # project's urls.py 
        path('firebase-messaging-sw.js', serviceWorker, name='service-worker'), 

3.  Render an HTML file with all the firebaseConfig included, as has been done in the notification app.\
    make sure "vapidKey" included in html tempalte for generating the "FCMToken". You can get "vapidKey" from :

        a. Open the Firebase console (https://console.firebase.google.com/). 
        b. Click on the project you have created. 
        c. Click on the "settings icon" and then click on "Project settings." 
        d. select "Cloud Messaging" tab scroll down in "Web Push certificates" section and copy the vapidKey

                    