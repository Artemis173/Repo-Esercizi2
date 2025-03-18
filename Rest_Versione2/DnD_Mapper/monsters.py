import random

class Equipment:
    def __init__(self, name, attack_bonus, defense_bonus, dex_changes):
        self.name = name
        self.attack_bonus = attack_bonus
        self.defense_bonus = defense_bonus
        self.dex_changes = dex_changes

class Monster:
    def __init__(self, name, hp, strength, dex, intelligence, equipment):
        self.name = name
        self.hp = hp
        self.strength = strength
        self.dex = dex
        self.intelligence = intelligence
        self.equipment = equipment

# Lista di mostri disponibili
MONSTER_LIST = [
    Monster("Goblin Guerriero", 10, 12, 10, 6, [Equipment("Spada corta", 1, 0, 0)]),
    Monster("Goblin Lanciere", 8, 10, 12, 6, [Equipment("Lancia", 2, 0, -1)]),
    Monster("Orco Furioso", 20, 16, 8, 4, [Equipment("Mazza Chiodata", 3, 1, -1)]),
    Monster("Re dei Goblin", 25, 15, 12, 10, [Equipment("Spada Lunga", 3, 1, -1), Equipment("Armatura", 0, 4, -1)]),
    Monster("Scheletro Guerriero", 15, 12, 10, 6, [Equipment("Spada Arrugginita", 2, 0, 0)]),
    Monster("Ragno Gigante", 12, 10, 14, 2, [Equipment("Zanne Velenose", 1, 0, 0)])
]

def get_random_monsters():
    "Restituisce un numero casuale di mostri per un incontro."
    num_monsters = random.randint(1, 3)  # Tra 1 e 3 mostri per stanza
    return random.sample(MONSTER_LIST, num_monsters)
