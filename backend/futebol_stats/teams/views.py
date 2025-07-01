from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api_clients.api_football import get_team_info
from rest_framework.permissions import AllowAny

class TeamDetailView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, team_id):
        data = get_team_info(team_id)
        if "error" in data:
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        return Response(data)