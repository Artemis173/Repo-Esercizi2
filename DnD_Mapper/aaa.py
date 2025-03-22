import random
from characters_data import characters  # Importiamo i dati dei personaggi dal file esterno
from DnD_Mapper.artifacts import get_random_artifact
from DnD_Mapper.monsters import get_random_monsters

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
        self.equipment = [Equipment(**item) for item in equipment]
        self.gold = gold
        self.position = position

    def display_status(self):
        print(f"{self.name} ({self.char_class}) - HP: {self.hp}, Forza: {self.strength}, Destrezza: {self.dex}, Intelligenza: {self.intelligence}, Oro: {self.gold}")
        print("Equipaggiamento:")
        for item in self.equipment:
            print(f"  - {item.name} (Att: {item.attack_bonus}, Dif: {item.defense_bonus}, Dex: {item.dex_changes})")

    def heal_percentage(self, percentage=10):
        heal_amount = max(1, self.hp * percentage // 100)
        self.hp = min(self.hp + heal_amount, 20)
        print(f"{self.name} si è curato e ora ha {self.hp} HP.")

    def add_gold(self, amount):
        self.gold += amount
        print(f"{self.name} ha guadagnato {amount} oro. Totale: {self.gold} oro.")

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
    print("\n⚔️ Inizia il combattimento! ⚔️")
    turn_order = sorted(characters + monsters, key=lambda x: x.dex, reverse=True)

    while characters and monsters:
        for fighter in turn_order:
            if fighter in characters:
                if not monsters:
                    print("\n✅ Il gruppo ha vinto la battaglia!")
                    return True
                target = random.choice(monsters)
                damage = max(1, (fighter.strength + sum(item.attack_bonus for item in fighter.equipment)) - ((target.dex + sum(item.dex_changes for item in fighter.equipment)) // 2))
                target.hp -= damage
                print(f"{fighter.name} attacca {target.name} e infligge {damage} danni! ({target.hp} HP rimasti)")
                if target.hp <= 0:
                    print(f"💀 {target.name} è stato sconfitto!")
                    monsters.remove(target)
                    turn_order.remove(target)
            elif fighter in monsters:
                if not characters:
                    print("\n❌ Il gruppo è stato sconfitto...")
                    return False
                target = random.choice(characters)
                damage = max(1, (fighter.strength + sum(item.attack_bonus for item in fighter.equipment)) - ((target.dex + sum(item.dex_changes for item in fighter.equipment)) // 2))
                target.hp -= damage
                print(f"{fighter.name} attacca {target.name} e infligge {damage} danni! ({target.hp} HP rimasti)")
                if target.hp <= 0:
                    print(f"☠️ {target.name} è stato sconfitto!")
                    characters.remove(target)
                    turn_order.remove(target)
    return True if characters else False

def explore(characters):
    print("\n🔍 Esplorazione in corso...")
    # Simulazione dell'esplorazione (aggiungere logica delle stanze qui)
    print("L'esplorazione è terminata!")

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
