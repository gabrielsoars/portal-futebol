from rest_framework import serializers

# Serializer para extrair os dados de um jogador da resposta da API
class ApiPlayerSerializer(serializers.Serializer):
    id = serializers.IntegerField(source='player.id')
    name = serializers.CharField(source='player.name')
    photo = serializers.URLField(source='player.photo')
    # Adicionamos o time para dar mais contexto na lista de resultados
    team_name = serializers.CharField(source='statistics.0.team.name', default='Sem time')


# Serializer para extrair os dados de um time da resposta da API
class ApiTeamSerializer(serializers.Serializer):
    id = serializers.IntegerField(source='team.id')
    name = serializers.CharField(source='team.name')
    logo = serializers.URLField(source='team.logo')
    country = serializers.CharField(source='team.country')