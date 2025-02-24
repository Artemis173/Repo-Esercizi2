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
        self.equipment = equipment
        self.gold = gold

    def heal(self):
        heal_amount = random.randint(5, 10)
        self.hp += heal_amount
        print(f"{self.name} si è curato e ora ha {self.hp} HP.")

    
        # Aggiungere una nuova funzione per curare una percentuale fissa dell'HP
    def heal_percentage(character, percentage=10):
        heal_amount = character.hp * percentage // 100
        character.hp += heal_amount
        # Assicurati che l'HP non superi il massimo
        character.hp = min(character.hp, 20)
        print(f"{character.name} è curato del {percentage}% e ora ha {character.hp} HP.")

    def add_gold(self, amount):
        self.gold += amount
        print(f"{self.name} ha acquisito {amount} oro e ora ha {self.gold} oro.")

# Definizione della classe dei mostri
class Monster:
    def __init__(self, name, hp, strength, dex, intelligence, equipment):
        self.name = name
        self.hp = hp
        self.strength = strength
        self.dex = dex
        self.intelligence = intelligence
        self.equipment = equipment

# Creazione dei mostri
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

# Creazione dei personaggi
aric = Character("Aric", "Guerriero", 20, 15, 10, 8, [Equipment('Spada lunga', 3, 1), Equipment('Scudo', 0, 2), Equipment('Armatura a piastre', 0, 4)], 0)
lyra = Character("Lyra", "Mago", 12, 8, 12, 16, [Equipment('Bastone magico', 1, 0), Equipment('Mantello', 0, 1), Equipment('Libro degli incantesimi', 2, 0)], 0)
finn = Character("Finn", "Ladro", 15, 10, 16, 10, [Equipment('Pugnali', 2, 0), Equipment("Mantello dell'ombra", 0, 2), Equipment('Kit da scasso', 1, 0)], 0)

# Funzione per tirare il dado
def roll_dice(sides):
    return random.randint(1, sides)

# Funzione per il combattimento
def combat(characters, monsters):
    turn = 0
    while characters and monsters:
        attacker = characters[turn % len(characters)] if turn % 2 == 0 else monsters[turn % len(monsters)]
        defender = monsters[turn % len(monsters)] if turn % 2 == 0 else characters[turn % len(characters)]
        
        if attacker.hp > 0 and defender.hp > 0:
            roll = roll_dice(20)
            attack_bonus = 0
            if len(attacker.equipment) > 1:
                attack_bonus = sum(equip.attack_bonus for equip in attacker.equipment)
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
                defense_bonus = 0
                if len(defender.equipment) > 1:
                    defense_bonus = sum(equip.defense_bonus for equip in defender.equipment)
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

# Funzione per generare le stanze con i limiti richiesti
def generate_rooms():
    room_types = ["Stanza vuota", "Stanza del tesoro", "Stanza del mostro", "Stanza di ristoro rapido", "Stanza degli artefatti"]

    # Creiamo una lista di stanze, rispettando i limiti richiesti
    rooms = []

    # Aggiungi al massimo 1 "Stanza del tesoro"
    rooms.append("Stanza del tesoro")

    # Aggiungi al massimo 2 "Stanze vuote"
    rooms += ["Stanza vuota"] * 2

    # Aggiungi al massimo 2 "Stanze di ristoro rapido"
    rooms += ["Stanza di ristoro rapido"] * 2

    # Aggiungi al massimo 2 "Stanze degli artefatti"
    rooms += ["Stanza degli artefatti"] * 2

    # Aggiungi al massimo 10 "Stanze del mostro"
    rooms += ["Stanza del mostro"] * (15 - len(rooms))  # Per arrivare a un totale di 15 stanze

    # Mischia le stanze per renderle casuali
    random.shuffle(rooms)
    
    return rooms


# Generazione della mappa 10x10
def generate_map():
    room_types = ["Stanza vuota", "Stanza del tesoro", "Stanza del mostro", "Stanza di ristoro rapido"]
    map_size = 10
    dungeon_map = [[random.choice(room_types) for _ in range(map_size)] for _ in range(map_size)]
    dungeon_map[random.randint(0, 9)][random.randint(0, 9)] = "Stanza del tesoro"
    dungeon_map[random.randint(0, 9)][random.randint(0, 9)] = "Stanza del mostro con Re dei Goblin"
    dungeon_map[random.randint(0, 9)][random.randint(0, 9)] = "Stanza degli artefatti"
    return dungeon_map

def heal_percentage(character, percentage=10):
    heal_amount = character.hp * percentage // 100
    character.hp += heal_amount
    # Assicurati che l'HP non superi il massimo
    character.hp = min(character.hp, 20)
    print(f"{character.name} è curato del {percentage}% e ora ha {character.hp} HP.")

# Funzione di esplorazione aggiornata con la cura nella "Stanza di ristoro rapido"
def explore(characters):
    print("Esplorazione delle stanze:")
    directions = ["sinistra", "destra", "sopra", "sotto"]
    dungeon_map = generate_map()
    explored_rooms = set()
    current_position = (0, 0)
    room_count = 0

    while room_count < 15:
        if current_position in explored_rooms:
            print(f"Sei tornato in una stanza già conquistata.")
            current_position = move_position(current_position, directions)
        
        room = dungeon_map[current_position[0]][current_position[1]]
        explored_rooms.add(current_position)
        print(f"Sei in una {room}.")
        
        if room == "Stanza del mostro" or room == "Stanza del mostro con Re dei Goblin":
            if room == "Stanza del mostro con Re dei Goblin":
                monster = Monster("Re dei Goblin", 20, 15, 12, 10, [Equipment("Spada lunga", 3, 1), Equipment("Armatura", 0, 4)])
            else:
                monster = create_monster()
            print(f"Un {monster.name} appare!")
            monsters = [monster]
            if not combat(characters, monsters):
                break
        
        # Aggiunta di oro nella stanza del tesoro
        if room == "Stanza del tesoro" and current_position not in explored_rooms:
            for character in characters:
                character.add_gold(100)  # Aggiungi oro ai personaggi
        
        # Cura nella stanza di ristoro rapido
        if room == "Stanza di ristoro rapido" and current_position not in explored_rooms:
            print("Sei entrato nella Stanza di Ristoro Rapido!")
            for character in characters:
                heal_percentage(character, 10)  # Cura il 10% della salute del personaggio

            roll = roll_dice(20)
            if roll <= 10:
                print("Sei stato imboscato!") 
                monster = create_monster()
                monsters = [monster]
                if not combat(characters, monsters):
                    break
        
        if room == "Stanza degli artefatti":
            for character in characters:
                search_artifact(character)
        
        # Logica per curare un personaggio se ha pochi HP
        for character in characters:
            if character.hp < 10:
                heal_decision = input(f"{character.name} ha {character.hp} HP. Vuoi curarti? (s/n): ").lower()
                if heal_decision == 's':
                    character.heal()

        print("\npos: ", current_position)
        direction = input("In quale direzione vuoi andare? (sinistra/destra/sopra/sotto): ").lower()
        if direction not in directions:
            print("Direzione non valida. Riprova.")
        else:
            current_position = move_position(current_position, direction)
        
        continue_exploring = input("Vuoi continuare ad esplorare? (s/n): ").lower()
        if continue_exploring != 's':
            break
        
        room_count += 1

def move_position(current_position, direction):
    x, y = current_position
    if direction == "sinistra":
        if y-1 < 0:
            y = 0
            print("C'è un cazzo di muro dove vuoi andare?")
        else:
            y -= 1
    elif direction == "destra":
        if y+1 > 9:
            y = 9
            print("C'è un cazzo di muro dove vuoi andare?")
        else:
            y += 1
    elif direction == "sopra":
        if x+1 > 9:
            x = 9
            print("C'è un cazzo di muro dove vuoi andare?")
        else:
            x += 1
    elif direction == "sotto":
        if x-1 < 0:
            x = 0
            print("C'è un cazzo di muro dove vuoi andare?")
        else:
            x -= 1
    return (x, y)

# Funzione per la ricerca dell'artefatto
def search_artifact(character):
    roll = roll_dice(20)
    if roll + character.intelligence > 15:
        print(f"{character.name} trova l'artefatto magico!")
    else:
        print(f"{character.name} non riesce a trovare l'artefatto.")

# Funzione per stampare lo stato dei personaggi
def print_character_status(character):
    print(f"{character.name}: HP: {character.hp}, Oro: {character.gold}")

# Stato iniziale dei personaggi
print("Stato iniziale dei personaggi:")
print_character_status(aric)
print_character_status(lyra)
print_character_status(finn)

# Simulazione dell'esplorazione
characters = [aric, lyra, finn]
explore(characters)

# Ricerca dell'artefatto
#print("Ricerca dell'artefatto:")
#search_artifact(aric) 
#search_artifact(lyra)
#search_artifact(finn)

# Stato finale dei personaggi
print("Stato finale dei personaggi:")
print_character_status(aric)
print_character_status(lyra)
print_character_status(finn)


