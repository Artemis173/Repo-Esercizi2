import random
from artifacts import get_random_artifact

class Equipment:
    def __init__(self, name, attack_bonus, defense_bonus):
        self.name = name
        self.attack_bonus = attack_bonus
        self.defense_bonus = defense_bonus

class Character:
    def __init__(self, name, char_class, hp, strength, dex, intelligence, equipment, gold, position):
        self.name = name
        self.char_class = char_class
        self.hp = hp
        self.strength = strength
        self.dex = dex
        self.intelligence = intelligence
        self.equipment = equipment
        self.gold = gold
        self.position = position

    def heal_percentage(self, percentage=10):
        heal_amount = max(1, self.hp * percentage // 100)
        self.hp = min(self.hp + heal_amount, 20)
        print(f"{self.name} si è curato e ora ha {self.hp} HP.")

    def add_gold(self, amount):
        self.gold += amount
        print(f"{self.name} ha guadagnato {amount} oro. Totale: {self.gold} oro.")

    def display_status(self):
        print(f"{self.name} ({self.char_class}) - HP: {self.hp}, Forza: {self.strength}, Destrezza: {self.dex}, Intelligenza: {self.intelligence}, Oro: {self.gold}")
        print("Equipaggiamento:")
        for item in self.equipment:
            print(f" - {item.name} (Att: {item.attack_bonus}, Dif: {item.defense_bonus})")

    def add_equipment(self, equipment):
        self.equipment.append(equipment)
        print(f"{self.name} ha ottenuto l'artefatto: {equipment.name}!")

class Monster:
    def __init__(self, name, hp, strength, dex, intelligence, equipment):
        self.name = name
        self.hp = hp
        self.strength = strength
        self.dex = dex
        self.intelligence = intelligence
        self.equipment = equipment

def create_monster():
    monsters = [
        ("Goblin Guerriero", 10, 12, 10, 6, [Equipment('Spada corta', 1, 0)]),
        ("Goblin Lancieri", 8, 10, 12, 6, [Equipment('Lancia', 2, 0)]),
        ("Re dei Goblin", 20, 15, 12, 10, [Equipment("Spada lunga", 3, 1), Equipment("Armatura", 0, 4)])
    ]
    return Monster(*random.choice(monsters))

def roll_dice(sides):
    return random.randint(1, sides)

def explore(characters):
    explored_rooms = {}
    room_limits = {
        "Stanza del tesoro": 2,
        "Stanza degli artefatti": 2,
        "Stanza di ristoro": 2,
        "Stanza della cupidigia": 3,
        "Stanza vuota": 4
    }
    room_types = list(room_limits.keys()) + ["Stanza del mostro"]
    
    for _ in range(5):
        room = random.choice(room_types)
        if room not in explored_rooms:
            explored_rooms[room] = 0
        
        if explored_rooms[room] >= room_limits.get(room, float('inf')):
            print(f"\n📍 Il gruppo torna nella {room}, ma non c'è nulla di nuovo.")
            continue
        
        explored_rooms[room] += 1
        print(f"\n📍 Il gruppo entra in una {room}.")
        
        if room == "Stanza del mostro":
            monsters = [create_monster()]
            print(f"Un {monsters[0].name} appare!")
        elif room == "Stanza del tesoro":
            for char in characters:
                char.add_gold(50)
        elif room == "Stanza di ristoro":
            for char in characters:
                char.heal_percentage(20)
        elif room == "Stanza degli artefatti":
            if roll_dice(20) > 15:
                artifact = get_random_artifact()
                character = random.choice(characters)
                character.add_equipment(artifact)
            else:
                print("❌ Nessun artefatto trovato.")
        elif room == "Stanza della cupidigia":
            for char in characters:
                if char.hp > 1:
                    char.hp //= 2
                    char.add_gold(100)
    
    print("🏁 Esplorazione completata!")

spawn_position = (random.randint(0, 15), random.randint(0, 15))
thalion = Character("Thalion", "Guerriero", 20, 16, 10, 8, [Equipment("Spada", 2, 0)], 50, spawn_position)
elara = Character("Elara", "Mago", 15, 8, 14, 16, [Equipment("Bastone", 1, 0)], 20, spawn_position)
finnian = Character("Finnian", "Ladro", 18, 14, 16, 10, [Equipment("Pugnale", 1, 0)], 30, spawn_position)

explore([thalion, elara, finnian])
