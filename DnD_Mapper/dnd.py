import random

class Equipment:
    def __init__(self, name, attack_bonus, defense_bonus):
        self.name = name
        self.attack_bonus = attack_bonus
        self.defense_bonus = defense_bonus

class Character:
    def __init__(self, name, char_class, hp, strength, dex, intelligence, equipment, gold):
        self.name = name
        self.char_class = char_class
        self.hp = hp
        self.strength = strength
        self.dex = dex
        self.intelligence = intelligence
        self.equipment = equipment  # Cambiato 'equip' in 'equipment'
        self.gold = gold

    def heal(self):
        heal_amount = random.randint(5, 10)
        self.hp += heal_amount
        print(f"{self.name} si è curato e ora ha {self.hp} HP.")
    
    # Aggiunta funzione per curare una percentuale dell'HP
    def heal_percentage(self, percentage=10):
        heal_amount = self.hp * percentage // 100
        self.hp += heal_amount
        # Assicurati che l'HP non superi il massimo
        self.hp = min(self.hp, 20)
        print(f"{self.name} è curato del {percentage}% e ora ha {self.hp} HP.")

    def add_gold(self, amount):
        self.gold += amount
        print(f"{self.name} ha acquisito {amount} oro e ora ha {self.gold} oro.")

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
        ("Goblin Arcieri", 6, 8, 14, 6, [Equipment('Arco e frecce', 1, 0)]),
        ("Goblin", 8, 8, 12, 6, [Equipment('Mani', 0, 0)]),
        ("Goblin Sciamani", 10, 6, 10, 14, [Equipment('Bastone magico', 1, 0)]),
        ("Re dei Goblin", 20, 15, 12, 10, [Equipment("Spada lunga", 3, 1), Equipment("Armatura", 0, 4)])
    ]
    name, hp, strength, dex, intelligence, equipment = random.choice(monsters)
    return Monster(name, hp, strength, dex, intelligence, equipment)

def roll_dice(sides):
    return random.randint(1, sides)

def combat(characters, monsters):
    print("\n⚔️ Inizia il combattimento!")

    while any(char.hp > 0 for char in characters) and any(mon.hp > 0 for mon in monsters):
        # 🏹 Il gruppo attacca prima
        print("\n🔥 Il gruppo attacca!")
        for character in characters:
            if character.hp > 0:
                target = random.choice(monsters)  # Scegli un mostro casuale
                attack(character, target)

        # ☠️ Rimuove mostri sconfitti
        monsters = [mon for mon in monsters if mon.hp > 0]
        if not monsters:
            print("🎉 Il gruppo ha sconfitto tutti i mostri!")
            return True

        # 💀 I mostri attaccano il gruppo
        print("\n⚠️ I mostri attaccano!")
        for monster in monsters:
            target = random.choice(characters)  # Sceglie un eroe casuale
            attack(monster, target)

        # ☠️ Rimuove eroi sconfitti
        characters = [char for char in characters if char.hp > 0]
        if not characters:
            print("❌ Il gruppo è stato sconfitto!")
            return False

def attack(attacker, defender):
    roll = roll_dice(20)
    attack_bonus = sum(equip.attack_bonus for equip in attacker.equipment)

    if isinstance(attacker, Character):
        if attacker.char_class == "Guerriero":
            attack_roll = roll + attacker.strength + attack_bonus
        elif attacker.char_class == "Mago":
            attack_roll = roll + attacker.intelligence + attack_bonus
        elif attacker.char_class == "Ladro":
            attack_roll = roll + attacker.dex + attack_bonus
        else:
            attack_roll = roll + attack_bonus
    else:
        attack_roll = roll + attacker.strength + attack_bonus

    if attack_roll > 10:  # Supponiamo CA = 10
        damage = roll_dice(8)
        defense_bonus = sum(equip.defense_bonus for equip in defender.equipment)
        actual_damage = max(0, damage - defense_bonus)
        defender.hp -= actual_damage
        print(f"{attacker.name} attacca {defender.name} e infligge {actual_damage} danni!")
        if defender.hp <= 0:
            print(f"💀 {defender.name} è stato sconfitto!")
    else:
        print(f"{attacker.name} attacca {defender.name} ma manca!")

def print_character_status(character):
    print(f"{character.name}: HP: {character.hp}, Oro: {character.gold}")

def explore(characters):
    directions = ["sinistra", "destra", "sopra", "sotto"]
    dungeon_map = generate_map()  # Crea la mappa del dungeon
    explored_rooms = set()  # Set per stanze esplorate
    current_position = (0, 0)  # Posizione iniziale del gruppo
    room_count = 0

    while room_count < 15:
        print("\n💠 Il gruppo esplora il dungeon...")

        if current_position in explored_rooms:
            print("🔄 Il gruppo è tornato in una stanza già esplorata.")
        explored_rooms.add(current_position)

        room = dungeon_map[current_position[0]][current_position[1]]
        print(f"📍 Il gruppo è entrato in una {room}.")

        # ⚔️ Stanza del mostro
        if room in ["Stanza del mostro", "Stanza del mostro con Re dei Goblin"]:
            if room == "Stanza del mostro con Re dei Goblin":
                monster = Monster("Re dei Goblin", 20, 15, 12, 10, [Equipment("Spada lunga", 3, 1), Equipment("Armatura", 0, 4)])
            else:
                monster = create_monster()

            print(f"⚠️ Un {monster.name} appare!")
            monsters = [monster]

            # Il gruppo combatte unito
            if not combat(characters, monsters):
                print("❌ Il gruppo è stato sconfitto. Fine esplorazione.")
                break  # Se il gruppo perde, si interrompe l'esplorazione

        # 💰 Stanza del tesoro (oro per tutti)
        elif room == "Stanza del tesoro":
            for character in characters:
                character.add_gold(100)

        # 🛏️ Stanza di ristoro (cura il gruppo)
        elif room == "Stanza di ristoro rapido":
            print("🌿 Il gruppo si riposa nella Stanza di Ristoro!")
            for character in characters:
                character.heal_percentage(10)

        # 🏺 Stanza degli artefatti (tutti cercano artefatti)
        elif room == "Stanza degli artefatti":
            for character in characters:
                search_artifact(character)

        # Cura opzionale per i personaggi feriti
        for character in characters:
            if character.hp < 10:
                heal_decision = input(f"{character.name} ha {character.hp} HP. Vuoi curarlo? (s/n): ").lower()
                if heal_decision == 's':
                    character.heal()

        # 🌍 Mostra la posizione
        print(f"\n📍 Posizione attuale del gruppo: {current_position}")

        # ➡️ Scelta della direzione (unica per tutto il gruppo)
        direction = input("In quale direzione vuoi andare? (sinistra/destra/sopra/sotto): ").lower()
        if direction in directions:
            current_position = move_position(current_position, direction)
        else:
            print("🚫 Direzione non valida. Riprova.")

        # ⏳ Vuoi continuare?
        continue_exploring = input("Vuoi continuare ad esplorare? (s/n): ").lower()
        if continue_exploring != 's':
            print("🏁 Il gruppo termina l'esplorazione.")
            break

        room_count += 1

def move_position(current_position, direction):
    x, y = current_position
    if direction == "sinistra":
        if y-1 < 0:
            y = 0
        else:
            y -= 1
    elif direction == "destra":
        if y+1 > 9:
            y = 9
        else:
            y += 1
    elif direction == "sopra":
        if x-1 < 0:
            x = 0
        else:
            x -= 1
    elif direction == "sotto":
        if x+1 > 9:
            x = 9
        else:
            x += 1
    return (x, y)

def search_artifact(character):
    roll = roll_dice(20)
    if roll + character.intelligence > 15:
        print(f"{character.name} trova l'artefatto magico!")
    else:
        print(f"{character.name} non riesce a trovare l'artefatto.")

def generate_map():
    # Tipi di stanze disponibili
    room_types = ["Stanza vuota", "Stanza del mostro", "Stanza del mostro con Re dei Goblin", "Stanza del tesoro", "Stanza di ristoro rapido", "Stanza degli artefatti"]
    
    # Crea una mappa vuota
    map_grid = [["Stanza vuota" for _ in range(10)] for _ in range(10)]
    
    # Posiziona le stanze speciali
    special_rooms = [("Stanza del mostro", 3, 3), ("Stanza del mostro con Re dei Goblin", 5, 5), ("Stanza del tesoro", 1, 7), ("Stanza di ristoro rapido", 8, 8), ("Stanza degli artefatti", 2, 6)]
    for room_type, x, y in special_rooms:
        map_grid[x][y] = room_type
    
    # Genera stanze casuali
    for i in range(10):
        for j in range(10):
            if map_grid[i][j] == "Stanza vuota":
                room_type = random.choice(room_types)
                map_grid[i][j] = room_type

    return map_grid


def start_exploration(characters):
    # Ogni personaggio esplora contemporaneamente, quindi eseguiremo la funzione esplorativa per ciascuno di loro
    for character in characters:
        explore([character])  # Ogni personaggio esplora da solo, ma la funzione è chiamata separatamente per ciascuno


# Crea personaggi
thalion = Character("Thalion", "Guerriero", 20, 16, 10, 8, [Equipment("Spada", 2, 0)], 50)
elara = Character("Elara", "Mago", 15, 8, 14, 16, [Equipment("Bastone", 1, 0)], 20)
finnian = Character("Finnian", "Ladro", 18, 14, 16, 10, [Equipment("Pugnale", 1, 0)], 30)

# Lista di personaggi
characters = [thalion, elara, finnian]

# Avvia l'esplorazione
start_exploration(characters)

