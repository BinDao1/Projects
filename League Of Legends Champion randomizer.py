import requests
import random

Champion_url = "https://ddragon.leagueoflegends.com/cdn/15.2.1/data/en_US/champion.json"

def fetch_champions():
    response = requests.get(Champion_url)
    if response.status_code == 200:
        data = response.json()
        champions = list(data['data'].keys())
        return champions
    else:
        print('Error fetching champion data')
        return []

ROLE_MAP = {
    "Top": ["Garen", "Darius", "Shen", "Malphite", "Ornn"],
    "Jungle": ["Lee Sin", "Elise", "Rengar", "Graves", "Kha'Zix"],
    "Mid": ["Ahri", "Zed", "Syndra", "LeBlanc", "Viktor"],
    "ADC": ["Jinx", "Kai'Sa", "Lucian", "Ashe", "Ezreal"],
    "Support": ["Leona", "Thresh", "Nami", "Lulu", "Braum"]
}

def random_champion_by_role(role):
    role = role.capitalize()
    if role in ROLE_MAP:
        return random.choice(ROLE_MAP[role])
    return "Invalid role! Choose from: Top, Jungle, Mid, ADC, Support."

role = input("Enter role (Top, Jungle, Mid, ADC, Support): ")
print(f"Random {role} Champion:", random_champion_by_role(role))
