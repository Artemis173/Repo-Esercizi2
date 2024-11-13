create database cyaccademia

create domain NumberOre as integer
    default 0
    check (value >= 0 and value <= 8)

create domain Denaro as real
    check (value >= 0)

create domain StringaM as
    varchar(100)

create domain PostInteger as integer
    default 0
    check (value >= 0)

create type Strutturato as 
    enum ('Ricercatore', 'Professore Associato', 'Professore Ordinario')

create type LavoroProgetto as 
    enum ('Ricerca e Sviluppo', 'Dimostrazione', 'Management', 'Altro')

create type LavoroNonProgettuale as
    enum ('Didattica', 'Ricerca', 'Missione', 'Incontro Dipartimentale', 'Incontro Accademico', 'Altro')

create type CausaAssenza as 
    enum ('Chiusura Universitaria', 'Maternità', 'Malattia')

create table Persona (
    id PostInteger not null, 
    nome StringaM not null, 
    cognome StringaM not null, 
    posizione Strutturato not null,
    stipendio Denaro not null,
    primary key (id)
);

create table Progetto (
    id PostInteger not null,
    nome StringaM not null,
    inizio date not null,
    fine date not null,
    budget Denaro not null,
    check (inizio < fine),
    unique (nome),
    primary key (id)
);

create table Assenza (
    id PostInteger not null,
    persona PostInteger not null,
    tipo CausaAssenza not null,
    giorno date not null,
    primary key (id),
    unique (persona, giorno),
    foreign key (persona) references Persona(id)
);

create table WP (
    progetto PostInteger not null,
    id PostInteger not null,
    nome StringaM not null,
    inizio date not null,
    fine date not null,
    check (inizio < fine),
    unique (progetto, nome),
    primary key (progetto, id),
    foreign key (progetto) references Progetto(id)
);

create table AttivitàProgetto (
    id PostInteger not null,
    persona PostInteger not null,
    progetto PostInteger not null,
    wp PostInteger not null,
    giorno date not null,
    tipo LavoroProgetto not null,
    oreDurata NumberOre not null,
    foreign key (persona) references Persona(id),
    foreign key (progetto, wp) references WP(progetto, id)
);

create table AttivitàNonProgettuale (
    id PostInteger not null,
    persona PostInteger not null,
    tipo LavoroNonProgettuale not null,
    giorno date not null,
    oreDurata NumberOre not null,
    primary key (id),
    foreign key (persona) references Persona(id)
);

create table Assenza (
    id PostInteger not null,
    persona PostInteger not null,
    tipo CausaAssenza not null,
    giorno date not null,
    primary key (id),
    unique (persona, giorno),
    foreign key (persona) references Persona(id)
);