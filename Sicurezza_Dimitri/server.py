from flask import Flask, request, jsonify, render_template
import requests, os, base64
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

api = Flask("__name__")
base_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key="
sGoogleApiKey = "AIzaSyAO3tZD7UQH2dc6es-c1e0WeUmEL35vG44"
api_url = base_url + sGoogleApiKey

@api.route('/', methods=['GET'])
def index():
    return render_template('sendfile.html')

@api.route('/mansendfile', methods=['POST'])
def send_file():
    opzione = request.form.get('opzione')
    response_data = {}

    if opzione == 'opzione1':
        trama = request.form.get('label1')
        sArgomento2 = f"Crea una favola su {trama} in italiano"
        jsonDataRequest = {"contents": [{"parts": [{"text": sArgomento2}]}]}
        response = requests.post(api_url, json=jsonDataRequest, verify=False)
        if response.status_code == 200:
            dResponse = response.json()
            sTestoPrimaRisposta = dResponse['candidates'][0]['content']['parts'][0]['text']
            response_data = {"message": sTestoPrimaRisposta}
        else:
            response_data = {"message": f"Errore: {response.status_code}"}

    elif opzione == 'opzione2':
        domanda = request.form.get('label2')
        jsonDataRequest = {"contents": [{"parts": [{"text": domanda}]}]}
        response = requests.post(api_url, json=jsonDataRequest, verify=False)
        if response.status_code == 200:
            dResponse = response.json()
            sTestoPrimaRisposta = dResponse['candidates'][0]['content']['parts'][0]['text']
            response_data = {"message": sTestoPrimaRisposta}
        else:
            response_data = {"message": f"Errore: {response.status_code}"}

    elif opzione == 'opzione3':
        image_path = request.form.get('label3')
        domanda = request.form.get('label4')
        
        if os.path.exists(image_path):
            with open(image_path, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
            
            jsonDataRequest = {
                "contents": [{
                    "parts": [
                        {"text": domanda},
                        {"inline_data": {"mime_type": "image/jpeg", "data": encoded_string}}
                    ]
                }]
            }
            response = requests.post(api_url, json=jsonDataRequest, verify=False)
            if response.status_code == 200:
                dResponse = response.json()
                sTestoPrimaRisposta = dResponse['candidates'][0]['content']['parts'][0]['text']
                response_data = {"message": sTestoPrimaRisposta}
            else:
                response_data = {"message": f"Errore: {response.status_code}"}
        else:
            response_data = {"message": "Errore: File immagine non trovato"}

    else:
        response_data = {"message": "Opzione non valida"}

    return jsonify(response_data), 200, {'Content-Type': 'application/json; charset=utf-8'}

if __name__ == "__main__":
    api.run(host="0.0.0.0", port=8085)