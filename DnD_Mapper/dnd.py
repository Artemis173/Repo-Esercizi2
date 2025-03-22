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

def get_damage_dice(char_class):
    if char_class == "Guerriero":
        return 10
    elif char_class == "Ladro":
        return 12
    elif char_class == "Mago":
        return 8
    return 6  # Default damage dice

def combat(characters, monsters):
    print("\n⚔️ Inizia il combattimento!")
    while any(c.hp > 0 for c in characters) and any(m.hp > 0 for m in monsters):
        print("\n🔥 Il gruppo attacca!")
        for character in characters:
            if character.hp > 0:
                target = random.choice(monsters)
                attack(character, target)
        monsters = [m for m in monsters if m.hp > 0]
        if not monsters:
            print("🎉 Il gruppo ha vinto!")
            return True
        print("\n⚠️ I mostri attaccano!")
        for monster in monsters:
            target = random.choice([c for c in characters if c.hp > 0])
            attack(monster, target)
        characters = [c for c in characters if c.hp > 0]
        if not characters:
            print("❌ Il gruppo è stato sconfitto!")
            return False

def attack(attacker, defender):
    roll = roll_dice(20)
    attack_bonus = sum(e.attack_bonus for e in attacker.equipment)
    attack_roll = roll + attack_bonus + (attacker.strength if isinstance(attacker, Character) else attacker.strength)
    if attack_roll > 10:
        damage_dice = get_damage_dice(attacker.char_class) if isinstance(attacker, Character) else 8
        damage = roll_dice(damage_dice)
        defense_bonus = sum(e.defense_bonus for e in defender.equipment)
        actual_damage = max(0, damage - defense_bonus)
        defender.hp -= actual_damage
        print(f"{attacker.name} attacca {defender.name} e infligge {actual_damage} danni!")
        if defender.hp <= 0:
            print(f"💀 {defender.name} è stato sconfitto!")
    else:
        print(f"{attacker.name} attacca {defender.name} ma manca!")

def move_group(characters):
    directions = {"N": (0, 1), "S": (0, -1), "E": (1, 0), "O": (-1, 0)}
    while True:
        move = input("Dove vuoi muoverti? (N/S/E/O): ").upper()
        if move in directions:
            dx, dy = directions[move]
            new_x = max(0, min(15, characters[0].position[0] + dx))
            new_y = max(0, min(15, characters[0].position[1] + dy))
            for char in characters:
                char.position = (new_x, new_y)
            print(f"Il gruppo si è spostato in ({new_x}, {new_y})")
            return (new_x, new_y)
        else:
            print("Comando non valido. Riprova.")

def explore(characters):
    explored_rooms = {}
    room_limits = {
        "Stanza del Tesoro": 2,
        "Stanza degli Artefatti": 2,
        "Stanza della Cupidigia": 3,
        "Stanza Vuota": 4
    }
    room_counts = {room: 0 for room in room_limits}
    room_counts["Stanza del Mostro"] = 0
    room_types = list(room_limits.keys()) + ["Stanza del Mostro"]

    for _ in range(5):
        while True:
            action = input("Vuoi muoverti o vedere lo status? (M/S): ").upper()
            if action == "S":
                for char in characters:
                    char.display_status()
            elif action == "M":
                break
            else:
                print("Comando non valido. Riprova.")

        position = move_group(characters)
        if position is None:
            continue
        
        if position in explored_rooms:
            room = explored_rooms[position]
            if room == "Stanza Conquistata":
                print(f"\n📍 Il gruppo entra in una {room}. Non c'è più nulla!")
                continue
        else:
            available_rooms = [room for room in room_types if room_counts.get(room, 0) < room_limits.get(room, 0)]
            if not available_rooms or room_counts.get("Stanza di Ristoro", 0) >= 2:
                room = "Stanza del Mostro"
            else:
                room = random.choice(available_rooms)
                room_counts[room] += 1
            explored_rooms[position] = room
        
        print(f"\n📍 Il gruppo entra in una {room}.")
        
        if room == "Stanza del Mostro":
            print("\n👹 Il gruppo incontra dei mostri!")
            monsters = [create_monster()]
            if not combat(characters, monsters):
                print("❌ Il gruppo ha fallito l'esplorazione.")
                return
        elif room == "Stanza del Tesoro":
            for char in characters:
                char.add_gold(50)
        elif room == "Stanza degli Artefatti":
            if roll_dice(20) > 15:
                artifact = get_random_artifact()
                chosen_character = random.choice(characters)
                chosen_character.equipment.append(artifact)
                print(f"🔮 {chosen_character.name} ha trovato l'artefatto: {artifact.name}!")
            else:
                print("❌ Nessun artefatto trovato.")
        elif room == "Stanza della Cupidigia":
            for char in characters:
                if char.hp > 1:
                    char.hp //= 2
                    char.add_gold(100)

        if room in ["Stanza del Tesoro", "Stanza degli Artefatti", "Stanza della Cupidigia"]:
            explored_rooms[position] = "Stanza Conquistata"
    
    print("🏁 Esplorazione completata!")


spawn_position = (random.randint(0, 15), random.randint(0, 15))
thalion = Character("Thalion", "Guerriero", 20, 16, 10, 8, [Equipment("Spada", 2, 0)], 50, spawn_position)
elara = Character("Elara", "Mago", 15, 8, 14, 16, [Equipment("Bastone", 1, 0)], 20, spawn_position)
finnian = Character("Finnian", "Ladro", 18, 14, 16, 10, [Equipment("Pugnale", 1, 0)], 30, spawn_position)

explore([thalion, elara, finnian])