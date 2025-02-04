class Champion:
    """Represents a TFT champion with name, cost, and traits."""

    def __init__(self, name, cost, traits):
        self.name = name
        self.cost = cost
        self.traits = traits

    def __str__(self):
        """String representation of a champion."""
        return f"{self.name} (Cost: {self.cost}, Traits: {', '.join(self.traits)})"


class Team:
    """Represents a TFT team and calculates trait synergies."""

    def __init__(self):
        self.champions = []

    def add_champion(self, champion):
        """Adds a champion to the team."""
        if champion in self.champions:
            print(f"{champion.name} is already in the team!")
        else:
            self.champions.append(champion)
            print(f"{champion.name} added to the team.")

    def remove_champion(self, champion_name):
        """Removes a champion from the team by name."""
        self.champions = [champ for champ in self.champions if champ.name != champion_name]
        print(f"{champion_name} removed from the team.")

    def calculate_traits(self):
        """Calculates how many champions contribute to each trait and checks synergy activation."""
        trait_counts = {}
        for champ in self.champions:
            for trait in champ.traits:
                trait_counts[trait] = trait_counts.get(trait, 0) + 1

        print("\n**Trait Synergies**")
        for trait, count in trait_counts.items():
            print(f"{trait}: {count} champions")

    def display_team(self):
        """Displays all champions in the team."""
        print("\n**Current Team**")
        if not self.champions:
            print("No champions in the team.")
        else:
            for champ in self.champions:
                print(champ)


# Example Champions
yasuo = Champion("Yasuo", 2, ["Challenger", "Exile"])
sett = Champion("Sett", 3, ["Brawler", "Exile"])
ahri = Champion("Ahri", 4, ["Mage", "Spirit"])
samira = Champion("Samira", 3, ["Sharpshooter", "Daredevil"])
cho_gath = Champion("Cho'Gath", 3, ["Brawler", "Void"])

# Example Usage
my_team = Team()
my_team.add_champion(yasuo)
my_team.add_champion(sett)
my_team.add_champion(ahri)
my_team.add_champion(samira)
my_team.calculate_traits()
my_team.display_team()
