import requests
from decouple import config

# Suas funções existentes como get_match_info() podem continuar aqui...

def get_player_info(player_id):
    """
    Busca informações detalhadas de um jogador específico.
    (Exemplo de como sua função existente pode se parecer)
    """
    url = f"https://v3.football.api-sports.io/players?id={player_id}&season=2023" # Adicione uma season para melhores resultados
    headers = {
        'x-rapidapi-key': config('API_KEY_FUTEBOL'),
        'x-rapidapi-host': 'v3.football.api-sports.io'
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar detalhes do jogador: {e}")
        return None

# --- NOVAS FUNÇÕES DE BUSCA ABAIXO ---

def search_players_by_name(name):
    """
    Busca jogadores na API-Football pelo nome.
    """
    url = "https://v3.football.api-sports.io/players"
    headers = {
        'x-rapidapi-key': config('API_KEY_FUTEBOL'),
        'x-rapidapi-host': 'v3.football.api-sports.io'
    }
    params = {'search': name}
    
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar jogadores: {e}")
        return None

def search_teams_by_name(name):
    """
    Busca times na API-Football pelo nome.
    """
    url = "https://v3.football.api-sports.io/teams"
    headers = {
        'x-rapidapi-key': config('API_KEY_FUTEBOL'),
        'x-rapidapi-host': 'v3.football.api-sports.io'
    }
    params = {'search': name}
    
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar times: {e}")
        return None