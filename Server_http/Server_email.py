from flask import Flask, render_template, request

utenti = [["mariorossi@gmail.com", "dsrfed12ezahS01r", "pippo", "0"],["elenagialli@gmail.com", "abcdef12thS01n", "coca", "1"]]
utente = []

api = Flask("_name_")

@api.route('/registrati', methods=["GET"])
def registrazioni():
    utente = []

    utente.append(request.args.get("email"))
    utente.append (request.args.get ("CF"))
    utente.append(request.args.get ("passw"))
    utente.append("0")
    if utente in utenti:
        return render_template('regok.html')
    else:
        return render_template('regko.html')


@api.route('/', methods=['GET'])
def index():
    return render_template( 'index.html')

api. run(host="0.0.0.0", port=8085)