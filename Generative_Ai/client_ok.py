import requests, json, sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

base_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key="
google_api_key = "AIzaSyCV5i6JczKgsraRJ9tT6vgWT1eyLihT0Gc"

def EseguiOperazione(iOper, sServizio, dDatiToSend):
    try:
        if iOper == 1:
            response = requests.post(sServizio, json=dDatiToSend)
        if iOper == 2:
            response = requests.get(sServizio)
        if iOper == 3:
            response = requests.put(sServizio, json=dDatiToSend)
        if iOper == 4:
            response = requests.delete(sServizio, json=dDatiToSend)

        if response.status_code==200:
            print(response.json())
        else:
            print("Attenzione, errore " + str(response.status_code))
    except:
        print("Problemi di comunicazione con il server, riprova più tardi.")

iFlag = 0
while iFlag==0:
    print("\nOperazioni disponibili:")
    print("1. Crea una favola")
    print("2. Rispondere ad una domanda")
    print("3. Rispondere ad una domanda con un'immagine")
    print("4. Esci")


    try:
        iOper = int(input("Cosa vuoi fare? "))
    except ValueError:
        print("Inserisci un numero valido!")
        continue


    if iOper == 1:
        sArgomento = input("Inserisci argomento della favola: ")
        sArgomento2 = "Crea una favola su " + sArgomento + " in lingua italiana"
        api_url = base_url + google_api_key
        jsonDataRequest = {"contents": [{"parts": [{"text": sArgomento2}]}]}
        response =  requests.post(api_url, json=jsonDataRequest,verify=False)
        if response.status_code == 200:
            print(response.json())
            dResponse = response.json()
            dListaContenuti = dResponse['candidates'][0]
            sTestoPrimaRisposta = dListaContenuti['content']['parts'][0]['text']
            print(sTestoPrimaRisposta)

        # Richiesta dati cittadino
    elif iOper == 2:
        sDomanda = input("Inserisci la domanda: ")
        jsonDataRequest = {"question": sDomanda, "language": "it"}
        api_url = base_url + google_api_key
        response = requests.post(api_url, json=jsonDataRequest, verify=False)
        
        if response.status_code == 200:
            dResponse = response.json()
            sRisposta = dResponse['candidates'][0]['content']['parts'][0]['text']
            print("Risposta: " + sRisposta)
        else:
            print("Errore nella richiesta dei dati: " + str(response.status_code))

    # Rispondere ad una domanda con un'immagine
    elif iOper == 3:
        sDomandaImmagine = input("Inserisci la domanda per l'immagine: ")
        jsonDataRequest = {"question": sDomandaImmagine, "includeImage": True, "language": "it"}
        api_url = base_url + google_api_key
        response = requests.post(api_url, json=jsonDataRequest, verify=False)
        
        if response.status_code == 200:
            dResponse = response.json()
            sRispostaImmagine = dResponse['candidates'][0]['content']['parts'][0]['text']
            sUrlImmagine = dResponse['candidates'][0]['content']['image_url']  # Supponendo che l'API restituisca un URL per l'immagine
            print("Risposta: " + sRispostaImmagine)
            print("Immagine: " + sUrlImmagine)
        else:
            print("Errore nella richiesta dell'immagine: " + str(response.status_code))

    elif iOper == 4:
        print("Buona giornata!")
        iFlag = 1

    else:
        print("Operazione non disponibile, riprova.")

 


