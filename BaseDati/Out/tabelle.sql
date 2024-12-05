CREATE DOMAIN CodFis as varchar(16);

CREATE TYPE Indirizzo as (
    via varchar(30),
    indirizzo varchar(5),
    cap varchar(5)
);

CREATE TYPE Denaro as (
    importo numeric(10,2),
    currency varchar(3)
);

CREATE TABLE Nazione (
    nome varchar not null,
    PRIMARY KEY(nome)
);

CREATE TABLE Regione (
    nome varchar not null,
    nazione varchar not null,
    PRIMARY KEY(nome, nazione),
    FOREIGN KEY(nazione) REFERENCES Nazione(nome)
);

CREATE TABLE Citta (
    nome varchar not null,
    regione varchar not null,
    nazione varchar not null,
    PRIMARY KEY(nome, regione, nazione),
    FOREIGN KEY(regione, nazione) REFERENCES Regione(nome, nazione)
);

CREATE TABLE Sede (
    id serial PRIMARY KEY not null,
    nome varchar not null,
    indirizzo Indirizzo not null,
    citta varchar not null,
    regione varchar not null,
    nazione varchar not null,
    FOREIGN  KEY(citta, regione, nazione) REFERENCES Citta(nome, regione, nazione)
);

CREATE TABLE Sala (
    nome varchar not null,
    sede integer not null,
    PRIMARY KEY(nome, sede),
    FOREIGN KEY(sede) REFERENCES Sede(id)
);

CREATE TABLE Settore (
    id serial PRIMARY KEY not null,
    nome varchar not null,
    sala varchar not null,
    sede integer not null,
    unique(nome, sala, sede),
    FOREIGN KEY(sala, sede) REFERENCES Sala(nome, sede)
);

CREATE TABLE Posto (
    fila integer not null,
    colonna integer not null,
    settore integer not null,
    PRIMARY KEY(fila, colonna, settore),
    FOREIGN KEY(settore) REFERENCES Settore(id)
);

CREATE TABLE Utente (
    nome varchar not null,
    cognome varchar not null,
    cf CodFis not null,
    PRIMARY KEY(cf)
);

CREATE TABLE Prenotazione (
    id serial not null,
    evento integer not null,
    utente CodFis not null,
    PRIMARY KEY(id),
    FOREIGN KEY(utente) REFERENCES Utente(cf),
    FOREIGN KEY(evento) REFERENCES Evento(id)
);

CREATE TABLE Genere (
    nome varchar not null,
    PRIMARY KEY(nome)
);

CREATE TABLE TipologiaSpettacolo (
    nome varchar not null,
    PRIMARY KEY(nome)
);

CREATE TABLE Artista (
    id serial not null,
    nome varchar not null,
    cognome varchar not null,
    nome_arte varchar,
    PRIMARY KEY(id)
);

CREATE TABLE Spettacolo (
    nome varchar not null,
    durata_min integer not null,
    genere varchar not null,
    tipologiaspettacolo varchar not null,
    id serial not null,
    PRIMARY KEY(id),
    FOREIGN KEY(genere) REFERENCES Genere(nome),
    FOREIGN KEY(tipologiaspettacolo) REFERENCES TipologiaSpettacolo(nome)
);

CREATE TABLE Partecipa (
    artista integer not null,
    spettacolo integer not null,
    PRIMARY KEY(artista, spettacolo),
    FOREIGN KEY(artista) REFERENCES Artista(id),
    FOREIGN KEY(spettacolo) REFERENCES Spettacolo(id)
);

CREATE TABLE Evento (
    id serial not null,
    data_evento Date not null,
    ora Time not null,
    sala varchar not null,
    sede integer not null,
    spettacolo integer not null,
    PRIMARY KEY(id),
    FOREIGN KEY(spettacolo) REFERENCES Spettacolo(id),
    FOREIGN KEY(sala, sede) REFERENCES Sala(nome, sede)
);

CREATE TABLE TipoTariffa (
    nome varchar not null,
    PRIMARY KEY(nome)
);

CREATE TABLE Tariffa (
    tipo varchar not null,
    evento integer not null,
    settore integer not null,
    prezzo Denaro not null,
    PRIMARY KEY(settore, tipo, evento),
    FOREIGN KEY(evento)  REFERENCES Evento(id),
    FOREIGN KEY(settore) REFERENCES Settore(id),
    FOREIGN KEY(tipo) REFERENCES TipoTariffa(nome)
);

CREATE TABLE pre_posto (
    tipo varchar not null,
    settore integer not null,
    fila integer not null,
    colonna integer not null,
    PRIMARY KEY(settore, tipo, fila, colonna),
    FOREIGN KEY(settore) REFERENCES Settore(id),    
    FOREIGN KEY(tipo) REFERENCES TipoTariffa(nome)
);
