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
    turn = 0
    while characters and monsters:
        attacker = characters[turn % len(characters)] if turn % 2 == 0 else monsters[turn % len(monsters)]
        defender = monsters[turn % len(monsters)] if turn % 2 == 0 else characters[turn % len(characters)]
        
        if attacker.hp > 0 and defender.hp > 0:
            roll = roll_dice(20)
            attack_bonus = sum(equip.attack_bonus for equip in attacker.equipment)  # Usato 'equipment' al posto di 'equip'
            
            if isinstance(attacker, Character):
                if attacker.char_class == "Guerriero":
                    attack_roll = roll + attacker.strength + attack_bonus
                elif attacker.char_class == "Mago":
                    attack_roll = roll + attacker.intelligence + attack_bonus
                elif attacker.char_class == "Ladro":
                    attack_roll = roll + attacker.dex + attack_bonus
                else:
                    attack_roll = roll + attacker.strength + attack_bonus
            else:
                attack_roll = roll + attacker.strength + attack_bonus
            
            if attack_roll > 10:  # Supponiamo che la Classe Armatura (CA) sia 10
                damage = roll_dice(8)
                defense_bonus = sum(equip.defense_bonus for equip in defender.equipment)  # Usato 'equipment' al posto di 'equip'
                actual_damage = max(0, damage - defense_bonus)
                defender.hp -= actual_damage
                print(f"{attacker.name} attacca {defender.name} e infligge {actual_damage} danni!")
                if defender.hp <= 0:
                    print(f"{defender.name} è stato sconfitto!")
                    if isinstance(defender, Monster):
                        monsters.remove(defender)
                    else:
                        characters.remove(defender)
            else:
                print(f"{attacker.name} attacca {defender.name} ma manca!")
        
        turn += 1
        
        if not monsters:
            print("Tutti i mostri sono stati sconfitti!")
            return True
        elif not characters:
            print("Tutti i personaggi sono stati sconfitti!")
            return False

def print_character_status(character):
    print(f"{character.name}: HP: {character.hp}, Oro: {character.gold}")

def explore(characters):
    directions = ["sinistra", "destra", "sopra", "sotto"]
    dungeon_map = generate_map()  # Crea la mappa iniziale
    explored_rooms = set()  # Set per memorizzare le stanze esplorate
    room_count = 0

    # Ogni personaggio esplora per 15 stanze (o finché non vogliono fermarsi)
    while room_count < 15:
        for character in characters:
            # Ogni personaggio esplora
            print(f"\n{character.name} sta esplorando le stanze:")
            current_position = (0, 0)  # Iniziamo dalla posizione (0, 0)
            if current_position in explored_rooms:
                print(f"{character.name} è tornato in una stanza già conquistata.")
                # Sostituisci la stanza con una nuova stanza
                dungeon_map = generate_map()

            # Aggiungi la stanza alla lista di stanze esplorate
            explored_rooms.add(current_position)

            # Ottieni la stanza corrente dalla mappa
            room = dungeon_map[current_position[0]][current_position[1]]
            print(f"{character.name} è in una {room}.")

            # Gestione delle stanze speciali
            if room == "Stanza del mostro" or room == "Stanza del mostro con Re dei Goblin":
                if room == "Stanza del mostro con Re dei Goblin":
                    monster = Monster("Re dei Goblin", 20, 15, 12, 10, [Equipment("Spada lunga", 3, 1), Equipment("Armatura", 0, 4)])
                else:
                    monster = create_monster()
                print(f"Un {monster.name} appare!")
                monsters = [monster]
                if not combat([character], monsters):  # Passa solo il singolo personaggio per il combattimento
                    break

            if room == "Stanza del tesoro":
                character.add_gold(100)  # Aggiungi oro al personaggio

            if room == "Stanza di ristoro rapido":
                print(f"{character.name} è entrato nella Stanza di Ristoro Rapido!")
                character.heal_percentage(10)

            if room == "Stanza degli artefatti":
                search_artifact(character)

            # Cura opzionale per il personaggio
            if character.hp < 10:
                heal_decision = input(f"{character.name} ha {character.hp} HP. Vuoi curarti? (s/n): ").lower()
                if heal_decision == 's':
                    character.heal()

            # Stampa la posizione attuale
            print(f"\nPosizione di {character.name}: ", current_position)

            # Richiesta di direzione per il movimento
            direction = input(f"{character.name}, in quale direzione vuoi andare? (sinistra/destra/sopra/sotto): ").lower()
            if direction not in directions:
                print("Direzione non valida. Riprova.")
            else:
                current_position = move_position(current_position, direction)

            # Chiedi all'utente se vuole continuare a esplorare
            continue_exploring = input(f"{character.name}, vuoi continuare ad esplorare? (s/n): ").lower()
            if continue_exploring != 's':
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

