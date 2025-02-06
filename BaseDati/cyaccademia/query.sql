-- Query 1 --

select p.nome, p.cognome, p.stipendio
from Persona p
where p.stipendio <= 40000;

-- Query 2 --

select distinct p.id, p.nome, p.cognome, p.posizione, p.stipendio
from Persona p
join AttivitaProgetto ap on p.id = ap.persona
where p.stipendio <= 40000;

-- Query 3 --

select sum(pr.budget) Totale_Budget
from Progetto pr;

-- Query 4 --

select distinct p.id, p.nome, p.cognome, sum(pr.budget) Totale_Budget
from Persona p
join AttivitaProgetto ap on p.id = ap.persona
join Progetto pr on pr.id = ap.progetto
group by p.id, p.nome, p.cognome;

-- Query 5 --

select p.nome, p.cognome, count(ap.progetto) as Progetti
from Persona p, AttivitaProgetto ap
where p.id = ap.persona and p.posizione = 'Professore Ordinario'
group by p.nome, p.cognome;

-- Query 6 --

select p.nome, p.cognome
from Persona p
join Assenza a on a.persona = p.id
where p.id = a.persona and p.posizione = 'Professore Associato' and a.tipo = 'Malattia'
group by p.nome, p.cognome
having count(a.id) > 0;

-- Query 7 --

select p.nome, p.cognome, sum(ap.oreDurata) as Ore_Totali
from Persona p
join AttivitaProgetto ap on p.id = ap.persona
join Progetto pr on ap.progetto = pr.id
where ap.progetto = '5'
group by p.nome, p.cognome;

-- Query 8 --

select p.nome, p.cognome, avg(ap.oreDurata) as media_ore
from Persona p
join AttivitaProgetto ap on p.id = ap.persona
group by p.nome, p.cognome;

-- Query 9 --

select p.nome , p.cognome, sum(anp.oreDurata) as Totale_Ore
from Persona p
join AttivitaNonProgettuale anp ON p.id = anp.persona
where anp.tipo = 'Didattica'
group by p.nome, p.cognome;

-- Query 10 --

select p.nome, p.cognome, sum(oreDurata) as Totale_Ore
from Persona p
join AttivitaProgetto ap on p.id = ap.persona
where ap.wp = '5' and ap.progetto = '3'
group by p.nome, p.cognome;