import requests
from decouple import config

# Suas funções existentes como get_match_info() podem continuar aqui...
from datetime import datetime
from dotenv import load_dotenv
import os
from pathlib import Path

# Corrigido para alcançar a pasta onde está o .env
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(dotenv_path=BASE_DIR / '.env')

API_KEY = os.getenv('SECRET_KEY')
BASE_URL = 'https://v3.football.api-sports.io'

if not API_KEY:
    raise ValueError("API_KEY não definida no .env")

HEADERS = {
    'x-apisports-key': API_KEY
}

def get_matches_today():
    date = datetime.now().strftime('%Y-%m-%d')
    url = f'{BASE_URL}/fixtures?date={date}&timezone=America%2FSao_Paulo'
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    return {"error": "Erro ao buscar partidas"}

def get_team_info(team_id):
    url = f"{BASE_URL}/teams?id={team_id}"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    return {"error": "Erro ao buscar informações do time"}

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