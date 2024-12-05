--1--
select distinct WP.nome, WP.inizio, WP.fine
from WP, Progetto
where WP.progetto = Progetto.id
and Progetto.nome = 'Pegasus';

--2--
select distinct p.nome, p.cognome, p.posizione
from Persona p, AttivitaProgetto ap, Progetto pr
where p.id = ap.persona and ap.progetto = pr.id and pr.nome = 'Pegasus'
ORDER BY p.cognome DESC;

--3--
select p.nome, p.cognome, p.posizione
from Persona p, AttivitaProgetto ap, Progetto pr
where p.id = ap.persona and ap.progetto = pr.id and p.nome = 'Pegasus'
group by p.nome, p.cognome, p.posizione
having count(ap.id) > 1;

--4--
select distinct p.nome, p.cognome, p.posizione
from Persona p, Assenza a
where p.id = a.persona and p.posizione = 'Professore Ordinario' and a.tipo = 'Malattia';

--5--
select p.nome, p.cognome, p.posizione
from Persona p, Assenza a
where p.id = a.persona and p.posizione = 'Professore Ordinario' and a.tipo = 'Malattia'
group by p.nome, p.cognome, p.posizione
having count(a.id) > 1;

--6--
select distinct p.nome, p.cognome, p.posizione
from Persona p, AttivitaNonProgettuale anp
where p.id = anp.persona and p.posizione = 'Ricercatore' and anp.tipo = 'Didattica';

--7--
select p.nome, p.cognome, p.posizione
from Persona p, AttivitaNonProgettuale anp
where p.id = anp.persona and p.posizione = 'Ricercatore' and anp.tipo = 'Didattica'
group by p.nome, p.cognome, p.posizione
having count(anp.id) > 1;

--8--
select distinct p.nome, p.cognome
from Persona p, AttivitaProgetto ap, AttivitaNonProgettuale anp
where p.id = ap.persona and p.id = anp.persona and ap.giorno = anp.giorno;


--9--
select distinct p.nome, p.cognome, ap.giorno, pr.nome, anp.tipo, ap.oreDurata as oreProg, anp.oreDurata as oreNonProg
from Persona p, AttivitaProgetto ap, AttivitaNonProgettuale anp, Progetto pr
where p.id = ap.persona and p.id = anp.persona and ap.progetto = pr.id and ap.giorno = anp.giorno;


--10--
select distinct p.nome, p.cognome
from Persona p, AttivitaProgetto ap, Assenza a
where p.id = ap.persona and p.id = a.persona and ap.giorno = a.giorno;


--11--
select distinct p.nome, p.cognome, ap.giorno, pr.nome, a.tipo, ap.oreDurata
from Persona p, AttivitaProgetto ap, Assenza a, Progetto pr
where p.id = ap.persona and p.id = a.persona and ap.progetto = pr.id and ap.giorno = a.giorno;


--12--
select wp1.nome
from WP wp1, Progetto pr1, WP wp2, Progetto pr2
where wp1.progetto = pr1.id and wp1.nome = wp2.nome AND wp1.progetto <> wp2.progetto and wp2.progetto = pr2.id;
