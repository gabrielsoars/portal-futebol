import requests
from decouple import config

def get_matches_today():
    """
    Busca as partidas do dia na API-Football.
    """
    url = "https://v3.football.api-sports.io/fixtures"
    headers = {
        'x-rapidapi-key': config('API_KEY_FUTEBOL'),
        'x-rapidapi-host': 'v3.football.api-sports.io'
    }
    from datetime import date
    today = date.today().strftime("%Y-%m-%d")
    params = {'date': today, 'status': 'NS-LIVE-HT-FT-P-SUSP-INT'} # Pega todos os jogos do dia (não iniciados, ao vivo, etc.)
    
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar partidas do dia: {e}")
        return None

def get_match_info(match_id):
    """
    Busca informações detalhadas de uma partida específica na API-Football.
    """
    url = f"https://v3.football.api-sports.io/fixtures?id={match_id}"
    headers = {
        'x-rapidapi-key': config('API_KEY_FUTEBOL'),
        'x-rapidapi-host': 'v3.football.api-sports.io'
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar detalhes da partida: {e}")
        return None

def get_match_lineups(match_id):
    """
    Busca as escalações de uma partida específica na API-Football.
    """
    url = f"https://v3.football.api-sports.io/fixtures/lineups?fixture={match_id}"
    headers = {
        'x-rapidapi-key': config('API_KEY_FUTEBOL'),
        'x-rapidapi-host': 'v3.football.api-sports.io'
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar escalações da partida: {e}")
        return None

def get_player_info(player_id):
    """
    Busca informações detalhadas de um jogador específico.
    (Esta função já existia no seu ficheiro)
    """
    url = f"https://v3.football.api-sports.io/players?id={player_id}&season=2024"
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