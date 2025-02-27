from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
CORS(app)

# Configurazione del database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelli delle tabelle
class Persona(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cognome = db.Column(db.String(100), nullable=False)
    posizione = db.Column(db.String(100), nullable=False)
    stipendio = db.Column(db.Float, nullable=False)

class Progetto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    inizio = db.Column(db.String(10), nullable=False)
    fine = db.Column(db.String(10), nullable=False)
    budget = db.Column(db.Float, nullable=False)

class WP(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    progetto = db.Column(db.Integer, db.ForeignKey('progetto.id'), nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    inizio = db.Column(db.String(10), nullable=False)
    fine = db.Column(db.String(10), nullable=False)

class AttivitaProgetto(db.Model):
    __tablename__ = 'AttivitaProgetto'
    id = db.Column(db.Integer, primary_key=True)
    persona = db.Column(db.Integer, nullable=False)
    progetto = db.Column(db.Integer, db.ForeignKey('progetto.id'), nullable=False)
    wp = db.Column(db.Integer, db.ForeignKey('wp.id'), nullable=False)
    giorno = db.Column(db.String(10), nullable=False)
    tipo = db.Column(db.String(100), nullable=False)
    oreDurata = db.Column(db.Integer, nullable=False)

class AttivitaNonProgettuale(db.Model):
    __tablename__ = 'AttivitaNonProgettuale'
    id = db.Column(db.Integer, primary_key=True)
    persona = db.Column(db.Integer, nullable=False)
    tipo = db.Column(db.String(100), nullable=False)
    giorno = db.Column(db.String(10), nullable=False)
    oreDurata = db.Column(db.Integer, nullable=False)

class Assenza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    persona = db.Column(db.Integer, db.ForeignKey('persona.id'), nullable=False)
    tipo = db.Column(db.String(100), nullable=False)
    giorno = db.Column(db.String(10), nullable=False)

# Funzione per generare endpoint GET per ogni tabella
def create_get_all_endpoint(route, model):
    @app.route(route, methods=['GET'], endpoint=f"get_all_{model.__name__}")
    def get_all():
        records = model.query.all()
        result = []
        for record in records:
            record_dict = {}
            for column in model.__table__.columns:
                record_dict[column.name] = getattr(record, column.name)
            result.append(record_dict)
        return jsonify(result)

# Creazione dinamica degli endpoint GET
create_get_all_endpoint('/Persona', Persona)
create_get_all_endpoint('/Progetto', Progetto)
create_get_all_endpoint('/WP', WP)
create_get_all_endpoint('/AttivitaProgetto', AttivitaProgetto)
create_get_all_endpoint('/AttivitaNonProgettuali', AttivitaNonProgettuale)
create_get_all_endpoint('/Assenze', Assenza)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)