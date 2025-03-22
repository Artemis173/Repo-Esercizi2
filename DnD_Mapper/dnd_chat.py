import random
from DnD_Mapper.artifacts import get_random_artifact
from DnD_Mapper.monsters import get_random_monsters
from DnD_Mapper.characters_data import characters

class Equipment:
    def __init__(self, name, attack_bonus, defense_bonus, dex_changes):
        self.name = name
        self.attack_bonus = attack_bonus
        self.defense_bonus = defense_bonus
        self.dex_changes = dex_changes

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
        print(f"\033[1;32m{self.name}\033[0m (\033[1;36m{self.char_class}\033[0m)")

        print(f"❤️  HP: \033[1;31m{self.hp}\033[0m  | 💪 Forza: \033[1;34m{self.strength}\033[0m  | 🏃 Destrezza: \033[1;35m{self.dex}\033[0m  | 🧠 Intelligenza: \033[1;33m{self.intelligence}\033[0m  | 💰 Oro: \033[1;33m{self.gold}\033[0m")
        
        print("\033[1;33mEquipaggiamento:\033[0m")
        if self.equipment:
            for item in self.equipment:
                print(f"  - \033[1;37m{item.name}\033[0m (⚔️ Att: \033[1;31m{item.attack_bonus}\033[0m, 🛡️ Dif: \033[1;34m{item.defense_bonus}\033[0m), 🏃 Dex: \033[1;31m{item.dex_changes}\033[0m")
        else:
            print("  Nessun equipaggiamento.")


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
    print("\n⚔️ \033[1;33mInizia il combattimento!\033[0m ⚔️")  # Titolo in giallo

    # Creiamo una lista di turni ordinata per destrezza (dal più alto al più basso)
    turn_order = sorted(characters + monsters, key=lambda x: x.dex, reverse=True)

    def colorize(name, is_character):
        return f"\033[1;32m{name}\033[0m" if is_character else f"\033[1;31m{name}\033[0m"

    while characters and monsters:
        for fighter in turn_order:
            if fighter in characters:
                if not monsters:
                    print("\n✅ \033[1;32mIl gruppo ha vinto la battaglia!\033[0m")
                    return True
                target = random.choice(monsters)
                damage = max(1, (fighter.strength + sum(item.attack_bonus for item in fighter.equipment)) - ((target.dex + sum(item.dex_changes for item in fighter.equipment)) // 2))
                target.hp -= damage
                print(f"{colorize(fighter.name, True)} attacca {colorize(target.name, False)} e infligge {damage} danni! ({target.hp} HP rimasti)")

                if target.hp <= 0:
                    print(f"💀 {colorize(target.name, False)} è stato sconfitto!")
                    monsters.remove(target)
                    turn_order.remove(target)  # Rimuoviamo il mostro dai turni

            elif fighter in monsters:
                if not characters:
                    print("\n❌ \033[1;31mIl gruppo è stato sconfitto...\033[0m")
                    return False
                target = random.choice(characters)
                damage = max(1, (fighter.strength + sum(item.attack_bonus for item in fighter.equipment)) - ((target.dex + sum(item.dex_changes for item in fighter.equipment)) // 2))
                target.hp -= damage
                print(f"{colorize(fighter.name, False)} attacca {colorize(target.name, True)} e infligge {damage} danni! ({target.hp} HP rimasti)")

                if target.hp <= 0:
                    print(f"☠️ {colorize(target.name, True)} è stato sconfitto!")
                    characters.remove(target)
                    turn_order.remove(target)  # Rimuoviamo il personaggio dai turni

    return True if characters else False

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
        "Stanza di Ristoro": 2,
        "Stanza del Tesoro": 2,
        "Stanza degli Artefatti": 2,
        "Stanza della Cupidigia": 3,
        "Stanza Vuota": 4
    }
    room_counts = {room: 0 for room in room_limits}
    room_counts["Stanza del Mostro"] = 0
    room_types = list(room_limits.keys()) + ["Stanza del Mostro"]

    for _ in range(25):
        while True:
            action = input("Vuoi muoverti o vedere lo status? (M/S): ").upper()
            if action == "S":
                for char in characters:
                    char.display_status()
            elif action == "M":
                position = move_group(characters)
                #position.append(explored_rooms)
                if position is None:
                    continue
                
                if position in explored_rooms:
                    room = explored_rooms[position]
                    if room == "Stanza Conquistata":
                        print(f"\n📍 Il gruppo entra in una {room}. Non c'è più nulla!")
                        continue
                else:
                    available_rooms = [room for room in room_types if room_counts.get(room, 0) < room_limits.get(room, 0)]
                    if not available_rooms or any(room_counts.get(room, 0) >= room_limits[room] for room in room_limits):
                        room = "Stanza del Mostro"
                    else:
                        room = random.choice(available_rooms)
                        room_counts[room] += 1
                    explored_rooms[position] = room
                
                print(f"\n📍 Il gruppo entra in una {room}.")
                break
            else:
                print("Comando non valido. Riprova.")

        if room == "Stanza Conquistata":
            print(f"\n🏆 Il gruppo ha conquistato la stanza!")

        elif room == "Stanza Vuota":
            print(f"\n🚫 Il gruppo entra in una stanza. La stanza è vuota!")
                  
        elif room == "Stanza del Mostro":
            print(f"\n👹 Il gruppo incontra dei mostri!")
            monsters = get_random_monsters()
            if not combat(characters, monsters):
                print("❌ Il gruppo ha fallito l'esplorazione.")
                return
            
        elif room == "Stanza del Tesoro":
            print(f"\n🏆 Il gruppo ha trovato dell'oro!")
            for char in characters:
                char.add_gold(50)

        elif room == "Stanza di Ristoro":
            print("\n❓ Il gruppo ha trovato una Spiazzo desolato?")
            for char in characters:
                char.heal_percentage(20)
                print("\n❤️  Il gruppo si riposa e recupera la salute.")

        elif room == "Stanza degli Artefatti":
                    roll = (roll_dice(20) + characters.intelligence)
                    if roll > 15:
                        artifact = get_random_artifact()
                        chosen_character = random.choice(characters)
                        chosen_character.equipment.append(random.choice(artifact))
                        print(f"🔮 {chosen_character.name} ha trovato l'artefatto: {artifact.name} (ATK: {artifact.attack_bonus}, DEF: {artifact.defense_bonus} DEX: {artifact.dex_changes})!")
                    else:
                        print("❌ Nessun artefatto trovato.")

        elif room == "Stanza della Cupidigia":
            print(f"\n🏺 Il gruppo ha trovato un antico baule!")
            for char in characters:
                if char.hp > 1:
                    char.hp //= 2
                    char.add_gold(100)

    print("🏁 Esplorazione completata!")
    
def select_characters():
    available_characters = [Character(**char, position=(random.randint(0, 15), random.randint(0, 15))) for char in characters]
    chosen_characters = []

    print("\nSeleziona fino a 3 personaggi per il tuo gruppo:")
    for i, char in enumerate(available_characters):
        print(f"{i + 1}. {char.name} ({char.char_class})")
    
    while len(chosen_characters) < 3:
        choice = input("Inserisci il numero del personaggio da selezionare (o premi Invio per terminare): ")
        if not choice:
            break
        try:
            choice_index = int(choice) - 1
            if 0 <= choice_index < len(available_characters):
                chosen_characters.append(available_characters.pop(choice_index))
                print(f"✅ {chosen_characters[-1].name} aggiunto al gruppo!")
            else:
                print("❌ Scelta non valida.")
        except ValueError:
            print("❌ Inserisci un numero valido.")

    return chosen_characters

if __name__ == "__main__":
    selected_party = select_characters()
    if not selected_party:
        print("❌ Nessun personaggio selezionato. Uscita dal gioco.")
    else:
        print("\n🎲 Il gruppo è pronto all'esplorazione!")
        for char in selected_party:
            char.display_status()
        explore(selected_party)

# spawn_position = (random.randint(0, 15), random.randint(0, 15))
# thalion = Character("Thalion", "Guerriero", 40, 20, 10, 8, [Equipment("Spada", 2, 0, 0)], 50, spawn_position)
# elara = Character("Elara", "Mago", 26, 12, 14, 16, [Equipment("Bastone", 1, 0, 0)], 20, spawn_position)
# finnian = Character("Finnian", "Ladro", 32, 18, 16, 10, [Equipment("Pugnale", 1, 0, 0)], 30, spawn_position)

# explore([thalion, elara, finnian])SSSS