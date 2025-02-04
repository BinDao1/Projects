import random

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
