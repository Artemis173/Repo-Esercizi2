class Character:
    def __init__(self, name, char_class, hp, strength, dex, intelligence, equipment, gold):
        self.name = name
        self.char_class = char_class
        self.hp = hp
        self.strength = strength
        self.dex = dex
        self.intelligence = intelligence
        self.equipment = equipment
        self.gold = gold

class Equipment:
    def __init__(self, name, attack_bonus, defense_bonus, dex_changes):
        self.name = name
        self.attack_bonus = attack_bonus
        self.defense_bonus = defense_bonus
        self.dex_changes = dex_changes

CHARACHTER_LIST = [
    Character("Thalion", "Guerriero", 40, 20, 10, 8, [Equipment("Spada", 2, 0, 0)], 50),
    Character("Elara", "Mago", 26, 12, 14, 16, [Equipment("Bastone", 1, 0, 0)], 20),
    Character("Finnian", "Ladro", 32, 18, 16, 10, [Equipment("Pugnale", 1, 0, 0)], 30)
]