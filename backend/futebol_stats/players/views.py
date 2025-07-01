from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api_clients.api_football import get_player_info
from rest_framework.permissions import AllowAny

class PlayerDetailView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, player_id):
        # data = get_player_info(player_id)

        data = {
            "get": "players/profiles",
            "parameters": {
                "player": str(player_id)
            },
            "errors": [],
            "results": 1,
            "paging": {
                "current": 1,
                "total": 1
            },
            "response": [
                {
                    "player": {
                        "id": int(player_id),
                        "name": "L. Mitre",
                        "firstname": "Lisandro Nicolás",
                        "lastname": "Mitre",
                        "age": 30,
                        "birth": {
                            "date": "1995-12-18",
                            "place": "Paraná",
                            "country": "Argentina"
                        },
                        "nationality": "Argentina",
                        "height": None,
                        "weight": None,
                        "number": 25,
                        "position": "Goalkeeper",
                        "photo": f"https://media.api-sports.io/football/players/{player_id}.png"
                    }
                }
            ]
        }

        if "error" in data:
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        return Response(data)