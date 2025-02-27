import random

class Equipment:
    def __init__(self, name, attack_bonus, defense_bonus):
        self.name = name
        self.attack_bonus = attack_bonus
        self.defense_bonus = defense_bonus

    def __str__(self):
        return f"{self.name} (ATK: {self.attack_bonus}, DEF: {self.defense_bonus})"

# Lista degli artefatti con bonus specifici
ARTIFACTS = [
    Equipment("Anello del Potere", 3, 1),
    Equipment("Amuleto della Fortuna", 0, 2),
    Equipment("Spada Infuocata", 5, 0),
    Equipment("Scudo della Difesa", 0, 4),
    Equipment("Elmo dell’Intelligenza", 0, 3),
    Equipment("Guanti della Forza", 2, 1),
    Equipment("Stivali della Rapidità", 1, 1),
    Equipment("Mantello dell'Ombra", 0, 3),
    Equipment("Bacchetta dell'Arcano", 4, 0),
    Equipment("Talismano della Resistenza", 0, 5),
]

def get_random_artifact():
    """Restituisce un artefatto casuale dalla lista."""
    return random.choice(ARTIFACTS)
