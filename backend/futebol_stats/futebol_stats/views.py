from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

# Importe as novas funções do nosso cliente de API
from api_clients.api_football import search_players_by_name, search_teams_by_name

# Importe os novos serializers
from .serializers import ApiPlayerSerializer, ApiTeamSerializer


class SearchView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        query = request.query_params.get('q', None)

        if not query:
            return Response(
                {"error": "O parâmetro de busca 'q' é obrigatório."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # 1. Faz as duas chamadas para a API externa
        players_data = search_players_by_name(query)
        teams_data = search_teams_by_name(query)

        # 2. Processa e serializa os resultados
        serialized_players = []
        if players_data and players_data.get('response'):
            player_serializer = ApiPlayerSerializer(data=players_data['response'], many=True)
            if player_serializer.is_valid():
                serialized_players = player_serializer.data
            else:
                print("Erro de serialização de jogadores:", player_serializer.errors)


        serialized_teams = []
        if teams_data and teams_data.get('response'):
            team_serializer = ApiTeamSerializer(data=teams_data['response'], many=True)
            if team_serializer.is_valid():
                serialized_teams = team_serializer.data
            else:
                print("Erro de serialização de times:", team_serializer.errors)

        # 3. Combina os resultados em uma única resposta
        combined_data = {
            'players': serialized_players,
            'teams': serialized_teams,
        }

        return Response(combined_data, status=status.HTTP_200_OK)