from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class NotificationList(APIView):
    def get(self, request):
        print('----- inside the view working someting-----')
        
        return Response({"response": "working"}, status=status.HTTP_200_OK)

