import os
import mmap
import shutil
import sys
from pathlib import Path
import PyPDF2
import textract
from PIL import Image
import pytesseract
from datetime import datetime

def get_user_input():
    print("\n=== Ricerca File ===")
    
    while True:
        dir_partenza = input("\nInserisci il percorso dove cercare (es. /home/user/documenti): ").strip()
        if os.path.isdir(dir_partenza):
            break
        print("Errore: La directory specificata non esiste. Riprova.")
    
    stringa = input("\nInserisci la stringa da cercare: ").strip()
    
    while True:
        dir_output = input("\nInserisci il percorso dove salvare i risultati (es. /home/user/risultati): ").strip()
        try:
            os.makedirs(dir_output, exist_ok=True)
            break
        except Exception as e:
            print(f"Errore nella creazione della directory: {e}")
            print("Riprova con un percorso diverso.")
    
    return dir_partenza, stringa, dir_output

def search_in_pdf(file_path, search_string):
    try:
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for i, page in enumerate(reader.pages):
                text = page.extract_text().lower()
                if search_string.lower() in text:
                    print(f"Trovato in PDF pagina {i + 1}: {file_path}")
                    return True
    except Exception as e:
        print(f"Errore nella lettura del PDF {file_path}: {str(e)}")
    return False

def search_in_doc(file_path, search_string):
    try:
        text = textract.process(file_path).decode('utf-8').lower()
        if search_string.lower() in text:
            print(f"Trovato in DOC/DOCX: {file_path}")
            return True
    except Exception as e:
        print(f"Errore nella lettura del file DOC/DOCX {file_path}: {str(e)}")
    return False

def search_in_image(file_path, search_string):
    try:
        text = pytesseract.image_to_string(Image.open(file_path)).lower()
        if search_string.lower() in text:
            print(f"Trovato in immagine: {file_path}")
            return True
    except Exception as e:
        print(f"Errore nella lettura dell'immagine {file_path}: {str(e)}")
    return False

def save_result(file_path, found_type, search_string, log_file):
    """Log the search result to a file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(log_file, 'a', encoding='utf-8') as f:
            f.write(f"Data: {timestamp}\nFile trovato: {file_path}\nTipo: {found_type}\nStringa cercata: {search_string}\n")
            f.write("-" * 50 + "\n")
    except Exception as e:
        print(f"Errore nel salvare il risultato: {str(e)}")

def search_string_in_filename(filename, search_string):
    if search_string.lower() in filename.lower():
        print(f"Trovato nel nome: {filename}")
        return True
    return False

def search_string_in_file_content(file_path, search_string):
    file_ext = os.path.splitext(file_path)[1].lower()
    
    if file_ext in ['.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.gif']:
        return search_in_image(file_path, search_string)
    elif file_ext == ".pdf":
        return search_in_pdf(file_path, search_string)
    elif file_ext in [".doc", ".docx"]:
        return search_in_doc(file_path, search_string)
    else:
        return search_in_text_file(file_path, search_string)

def search_in_text_file(file_path, search_string):
    try:
        with open(file_path, 'rb') as f:
            mmapped_file = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
            found = search_string.lower().encode() in mmapped_file.read().lower()
            if found:
                print(f"Trovato in file: {file_path}")
            return found
    except Exception as e:
        print(f"Errore nella lettura del file {file_path}: {str(e)}")
    return False

def save_file(file_path, output_dir):
    try:
        output_path = os.path.join(output_dir, os.path.basename(file_path))
        shutil.copy2(file_path, output_path)
        print(f"Copiato {file_path} in {output_path}")
        return True
    except Exception as e:
        print(f"Errore durante la copia del file: {str(e)}")
        return False

def clear_directory(directory):
    try:
        if os.path.exists(directory):
            for filename in os.listdir(directory):
                file_path = os.path.join(directory, filename)
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
                print(f"Eliminato: {file_path}")
            print(f"\nDirectory {directory} svuotata con successo")
    except Exception as e:
        print(f"Errore nello svuotamento della directory: {e}")

def search_files(start_dir, search_string, output_dir):
    found_files_count = 0
    log_file = os.path.join(output_dir, "risultati_ricerca.txt")
    
    clear_directory(output_dir)

    with open(log_file, 'w', encoding='utf-8') as f:
        f.write(f"Ricerca iniziata il: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Directory di ricerca: {start_dir}\n")
        f.write(f"Stringa cercata: {search_string}\n")
        f.write("=" * 50 + "\n\n")

    for root, _, files in os.walk(start_dir):
        for filename in files:
            file_path = os.path.join(root, filename)

            if search_string_in_filename(filename, search_string):
                if save_file(file_path, output_dir):
                    save_result(file_path, "Nome file", search_string, log_file)
                    found_files_count += 1
            elif search_string_in_file_content(file_path, search_string):
                if save_file(file_path, output_dir):
                    save_result(file_path, "Contenuto", search_string, log_file)
                    found_files_count += 1

    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(f"\nRicerca completata il: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Totale file trovati: {found_files_count}\n")
        
    return found_files_count

def main():
    try:
        start_dir, search_string, output_dir = get_user_input()
        
        print(f"\nRicerca di '{search_string}' in {start_dir}")
        print(f"I file trovati saranno copiati in {output_dir}\n")
        
        found_count = search_files(start_dir, search_string, output_dir)
        
        print(f"\nRicerca completata. Trovati {found_count} file")
        
        while True:
            response = input("\nVuoi fare un'altra ricerca? (s/n): ").lower().strip()
            if response in ['s', 'n']:
                break
            print("Per favore, rispondi 's' per sì o 'n' per no.")
        
        if response == 's':
            main()  # Restart the program
        else:
            print("\nGrazie per aver usato il programma!")
            
    except KeyboardInterrupt:
        print("\n\nProgramma interrotto dall'utente.")
        sys.exit(0)
    except Exception as e:
        print(f"\nErrore imprevisto: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()