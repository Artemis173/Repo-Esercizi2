from flask import Flask, request, jsonify
from myjson import JsonSerialize, JsonDeserialize

sFileDati = "./dizionario.json"
api = Flask(__name__)

@api.route('/CercaCasaVendita', methods=['GET'])
def cerca_casa_vendita():
    data = JsonDeserialize(sFileDati)
    case_vendita = data.get("case_in_vendita", [])
    return jsonify(case_vendita), 200

@api.route('/CercaCasaAffitto', methods=['GET'])
def cerca_casa_affitto():
    data = JsonDeserialize(sFileDati)
    case_affitto = data.get("case_in_affitto", [])
    return jsonify(case_affitto), 200

@api.route('/VendutaCasa', methods=['POST'])
def vendita_casa():
    vendita = request.json
    data = JsonDeserialize(sFileDati)

    for casa in data.get("case_in_vendita", []):
        if casa["catastale"] == vendita["catastale"]:
            data.setdefault("vendite_casa", []).append({
                "catastale": vendita["catastale"],
                "data_vendita": vendita["data"],
                "filiale_proponente": vendita["filiale_proponente"],
                "filiale_venditrice": vendita["filiale_venditrice"],
                "prezzo_vendita": vendita["prezzo"]
            })
            
            data["case_in_vendita"].remove(casa)
            for filiale in data.get("filiali", []):
                if filiale["partita_iva"] == vendita["filiale_venditrice"]:
                    filiale["case_vendute"] = filiale.get("case_vendute", 0) + 1

            JsonSerialize(data, sFileDati)
            return jsonify({"message": "Vendita registrata con successo."}), 200

    return jsonify({"error": "Casa non trovata."}), 404

@api.route('/AffittataCasa', methods=['POST'])
def affittata_casa():
    affitto = request.json
    data = JsonDeserialize(sFileDati)

    for casa in data.get("case_in_affitto", []):
        if casa["catastale"] == affitto["catastale"]:
            data.setdefault("affitti_casa", []).append({
                "catastale": affitto["catastale"],
                "data_affitto": affitto["data"],
                "filiale_proponente": affitto["filiale_proponente"],
                "filiale_venditrice": affitto["filiale_venditrice"],
                "prezzo_affitto": affitto["prezzo"],
                "durata_contratto": affitto["durata_contratto"]
            })
            
            data["case_in_affitto"].remove(casa)
            for filiale in data.get("filiali", []):
                if filiale["partita_iva"] == affitto["filiale_venditrice"]:
                    filiale["case_affittate"] = filiale.get("case_affittate", 0) + 1

            JsonSerialize(data, sFileDati)
            return jsonify({"message": "Affitto registrato con successo."}), 200

    return jsonify({"error": "Casa non trovata."}), 404

@api.route('/AggiungiFiliale', methods=['POST'])
def aggiungi_filiale():
    filiale = request.json
    data = JsonDeserialize(sFileDati)

    for f in data.get("filiali", []):
        if f["partita_iva"] == filiale["partita_iva"]:
            return jsonify({"error": "Filiale già esistente."}), 400

    data.setdefault("filiali", []).append({
        "partita_iva": filiale["partita_iva"],
        "nome": filiale["nome"],
        "indirizzo_sede": filiale["indirizzo_sede"],
        "civico": filiale["civico"],
        "telefono": filiale["telefono"],
        "case_vendute": 0,
        "case_affittate": 0
    })

    JsonSerialize(data, sFileDati)
    return jsonify({"message": "Filiale aggiunta con successo."}), 200

@api.route('/AggiungiVenditaCasa', methods=['POST'])
def aggiungi_vendita_casa():
    vendita = request.json
    data = JsonDeserialize(sFileDati)

    for casa in data.get("case_in_vendita", []):
        if casa["catastale"] == vendita["catastale"]:
            return jsonify({"error": "Casa già presente in vendita."}), 400

    data.setdefault("vendite_casa", []).append({
        "catastale": vendita["catastale"],
        "data_vendita": vendita["data_vendita"],
        "filiale_proponente": vendita["filiale_proponente"],
        "filiale_venditrice": vendita["filiale_venditrice"],
        "prezzo_vendita": vendita["prezzo_vendita"]
    })

    JsonSerialize(data, sFileDati)
    return jsonify({"message": "Vendita aggiunta con successo."}), 200

@api.route('/AggiungiAffittoCasa', methods=['POST'])
def aggiungi_affitto_casa():
    affitto = request.json
    data = JsonDeserialize(sFileDati)

    for casa in data.get("case_in_affitto", []):
        if casa["catastale"] == affitto["catastale"]:
            return jsonify({"error": "Casa già presente in affitto."}), 400

    data.setdefault("affitti_casa", []).append({
        "catastale": affitto["catastale"],
        "data_affitto": affitto["data_affitto"],
        "filiale_proponente": affitto["filiale_proponente"],
        "filiale_venditrice": affitto["filiale_venditrice"],
        "prezzo_affitto": affitto["prezzo_affitto"],
        "durata_contratto": affitto["durata_contratto"]
    })

    JsonSerialize(data, sFileDati)
    return jsonify({"message": "Affitto aggiunto con successo."}), 200

@api.route('/ReportCaseVenduteAffittate', methods=['GET'])
def report_case_vendute_affittate():
    data = JsonDeserialize(sFileDati)

    report = []
    for filiale in data.get("filiali", []):
        report.append({
            "filiale": filiale["nome"],
            "case_vendute": filiale.get("case_vendute", 0),
            "case_affittate": filiale.get("case_affittate", 0)
        })

    return jsonify(report), 200

if __name__ == "__main__":
    api.run(host="127.0.0.1", port=8080)