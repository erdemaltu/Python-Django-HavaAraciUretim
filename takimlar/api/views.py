from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class PersonelTakimAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_team = request.user.takim.isim
        return Response({"takim": user_team})
