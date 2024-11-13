select distinct cognome
from Persona;

select nome, cognome
from Persona
where posizione = 'Ricercatore';

select *
from Persona
where posizione = 'Professore Associato' and cognome like 'V%';

select *
from Persona
where cognome like 'V%' and (posizione = 'Professore Associato' or posizione = 'Professore Ordinario');

select *
from Progetto
where fine < CURRENT_DATE;

select *
from Progetto
order by inizio ASC;

select *
from WP
order by nome ASC;

select distinct tipo
from Assenza;

select distinct tipo
from AttivitaProgetto;

select giorno
from AttivitaNonProgettuale
where tipo = 'Didattica';
