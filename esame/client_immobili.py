import requests
import json

base_url = "http://127.0.0.1:8080"

def stampa_menu():
    print("\nBenvenuto nel client!")
    print("1. Aggiungi Filiale")
    print("2. Aggiungi Casa in Vendita")
    print("3. Aggiungi Casa in Affitto")
    print("4. Cerca Case in Vendita")
    print("5. Cerca Case in Affitto")
    print("6. Vendita Casa")
    print("7. Affitto Casa")
    print("8. Report Case Vendute e Affittate")
    print("9. Esci")

def aggiungi_filiale():
    partita_iva = input("Partita IVA della filiale: ")
    nome = input("Nome della filiale: ")
    indirizzo = input("Indirizzo della sede: ")
    civico = input("Civico: ")
    telefono = input("Telefono: ")

    data = {
        "partita_iva": partita_iva,
        "nome": nome,
        "indirizzo_sede": indirizzo,
        "civico": civico,
        "telefono": telefono
    }

    response = requests.post(f"{base_url}/AggiungiFiliale", json=data)
    if response.status_code == 200:
        print("Filiale aggiunta con successo.")
    else:
        print(f"Errore: {response.json()}")

def aggiungi_vendita_casa():
    catastale = input("Codice catastale della casa: ")
    data_vendita = input("Data di vendita (YYYY-MM-DD): ")
    filiale_proponente = input("Filiale proponente: ")
    filiale_venditrice = input("Filiale venditrice: ")
    prezzo_vendita = float(input("Prezzo di vendita: "))

    data = {
        "catastale": catastale,
        "data_vendita": data_vendita,
        "filiale_proponente": filiale_proponente,
        "filiale_venditrice": filiale_venditrice,
        "prezzo_vendita": prezzo_vendita
    }

    response = requests.post(f"{base_url}/AggiungiVenditaCasa", json=data)
    if response.status_code == 200:
        print("Casa in vendita aggiunta con successo.")
    else:
        print(f"Errore: {response.json()}")

def aggiungi_affitto_casa():
    catastale = input("Codice catastale della casa: ")
    data_affitto = input("Data di affitto (YYYY-MM-DD): ")
    filiale_proponente = input("Filiale proponente: ")
    filiale_venditrice = input("Filiale affittatrice: ")
    prezzo_affitto = float(input("Prezzo di affitto mensile: "))
    durata_contratto = int(input("Durata del contratto in mesi: "))

    data = {
        "catastale": catastale,
        "data_affitto": data_affitto,
        "filiale_proponente": filiale_proponente,
        "filiale_venditrice": filiale_venditrice,
        "prezzo_affitto": prezzo_affitto,
        "durata_contratto": durata_contratto
    }

    response = requests.post(f"{base_url}/AggiungiAffittoCasa", json=data)
    if response.status_code == 200:
        print("Casa in affitto aggiunta con successo.")
    else:
        print(f"Errore: {response.json()}")

def cerca_case(tipo):
    if tipo == 'vendita':
        response = requests.get(f"{base_url}/CercaCasaVendita")
    elif tipo == 'affitto':
        response = requests.get(f"{base_url}/CercaCasaAffitto")
    
    if response.status_code == 200:
        case = response.json()
        if not case:
            print(f"Nessuna casa in {tipo} trovata.")
        else:
            for casa in case:
                print(f"Catastale: {casa['catastale']}, Prezzo: {casa.get('prezzo_vendita', casa.get('prezzo_affitto'))}")
    else:
        print(f"Errore: {response.json()}")

def vendere_casa():
    catastale = input("Codice catastale della casa da vendere: ")
    data_vendita = input("Data di vendita (YYYY-MM-DD): ")
    filiale_proponente = input("Filiale proponente: ")
    filiale_venditrice = input("Filiale venditrice: ")
    prezzo_vendita = float(input("Prezzo di vendita: "))

    data = {
        "catastale": catastale,
        "data": data_vendita,
        "filiale_proponente": filiale_proponente,
        "filiale_venditrice": filiale_venditrice,
        "prezzo": prezzo_vendita
    }

    response = requests.post(f"{base_url}/VendutaCasa", json=data)
    if response.status_code == 200:
        print("Casa venduta con successo.")
    else:
        print(f"Errore: {response.json()}")

def affittare_casa():
    catastale = input("Codice catastale della casa da affittare: ")
    data_affitto = input("Data di affitto (YYYY-MM-DD): ")
    filiale_proponente = input("Filiale proponente: ")
    filiale_venditrice = input("Filiale affittatrice: ")
    prezzo_affitto = float(input("Prezzo di affitto mensile: "))
    durata_contratto = int(input("Durata del contratto in mesi: "))

    data = {
        "catastale": catastale,
        "data": data_affitto,
        "filiale_proponente": filiale_proponente,
        "filiale_venditrice": filiale_venditrice,
        "prezzo": prezzo_affitto,
        "durata_contratto": durata_contratto
    }

    response = requests.post(f"{base_url}/AffittataCasa", json=data)
    if response.status_code == 200:
        print("Casa affittata con successo.")
    else:
        print(f"Errore: {response.json()}")

def report_case_vendute_affittate():
    response = requests.get(f"{base_url}/ReportCaseVenduteAffittate")
    if response.status_code == 200:
        report = response.json()
        for filiale in report:
            print(f"Filiale: {filiale['filiale']}, Case Vendute: {filiale['case_vendute']}, Case Affittate: {filiale['case_affittate']}")
    else:
        print(f"Errore: {response.json()}")

def main():
    while True:
        stampa_menu()
        scelta = input("Scegli un'opzione (1-9): ")
        
        if scelta == '1':
            aggiungi_filiale()
        elif scelta == '2':
            aggiungi_vendita_casa()
        elif scelta == '3':
            aggiungi_affitto_casa()
        elif scelta == '4':
            cerca_case('vendita')
        elif scelta == '5':
            cerca_case('affitto')
        elif scelta == '6':
            vendere_casa()
        elif scelta == '7':
            affittare_casa()
        elif scelta == '8':
            report_case_vendute_affittate()
        elif scelta == '9':
            print("Uscita...")
            break
        else:
            print("Opzione non valida!")

if __name__ == "__main__":
    main()
