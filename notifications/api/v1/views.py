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
        token = "cYWeXD9LQGBEGC6lPkD3LM:APA91bGDUYhCn53T3sLFXB3OPuNPw_tUviUYS5Wu0O1wMdSrXkUtid9HwVyh0Q4pxUHzZNg8P35sbnavOAu3JWz32__pB19i2sL0zz1kb5n3Ptuix87SCCWiXlDE8tniMEIp3uZV76zk"
        
        # Create the message to send
        message = messaging.Message(
            notification=messaging.Notification(
                title=notification['title'],
                body=notification['body'],
            ),
            data=data, 
            token=token,
        )
        try:
            # Send the notification
            messaging.send(message)
            print("Notification sent successfully")
            return Response({"success": True, "message": "Notification sent successfully", "data": []},
                            status=status.HTTP_200_OK)
        except Exception as e:
            # Return error response if any issue occurs
            return Response({"success": False, "message": str(e), "data": []},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
