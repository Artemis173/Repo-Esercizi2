
CREATE DOMAIN PostInteger AS integer check (value >= 0);

CREATE DOMAIN StringaM AS varchar(100); 

create domain Denaro as
  real check (value >= 0);

CREATE TYPE ruolo_tipo AS 
    ENUM ('Staff Gilda', 'Guerriero', 'Mago', 'Curatore', 'Talker', 'Capogilda');

CREATE TYPE missione_interna_tipo AS 
    ENUM ('Attività Pubbliche', 'Attività di Guardia', 'Altro');

CREATE TYPE missione_esterna_tipo AS 
    ENUM ('Taglia di Caccia', 'Taglia di Banditi', 'Taglia di Scorta', 'Pulizia Dungeon', 'Altro');

CREATE TYPE funzione_mercato_tipo AS 
    ENUM ('Vendita', 'Acquisto');

CREATE TABLE Gilde (
    id PostInteger not null,
    nome StringaM NOT NULL UNIQUE,
    tipo StringaM NOT NULL,
    fondazione DATE not null not null,
    primary key (id)
);

CREATE TABLE Persona (
    id PostInteger not null,
    nome StringaM NOT NULL,
    cognome StringaM NOT NULL,
    ruolo ruolo_tipo NOT NULL,
    stipendio Denaro NOT NULL,
    gilda_id PostInteger not null,
    primary key (id)
    FOREIGN KEY (gilda_id) REFERENCES Gilde(id) deferrable
);

CREATE TABLE Mercato (
    id PostInteger not null,
    nome StringaM NOT NULL,
    tipo StringaM NOT NULL,
    funzione funzione_mercato_tipo NOT NULL,
    primary  key (id)
);

CREATE TABLE Camere (
    id PostInteger not null,
    gilda_id PostInteger not null,
    numero INT NOT NULL,
    primary  key (id),
    FOREIGN KEY (gilda_id) REFERENCES Gilde(id) deferrable,
    UNIQUE (gilda_id, numero)
);

CREATE TABLE MissioniInterne (
    id PostInteger not null,
    gilda_id PostInteger not null,
    tipo missione_interna_tipo NOT NULL,
    data DATE not null,
    ricompensa Denaro not null, 
    primary  key (id),
    FOREIGN KEY (gilda_id) REFERENCES Gilde(id) deferrable
);

CREATE TABLE MissioniEsterne (
    id PostInteger not null,
    gilda_id PostInteger not null,
    tipo missione_esterna_tipo NOT NULL,
    data DATE not null,
    ricompensa Denaro not null,
    primary  key (id),
    FOREIGN KEY (gilda_id) REFERENCES Gilde(id) deferrable
);

commit;