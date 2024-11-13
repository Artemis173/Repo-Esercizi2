-- 1. --
-- Qual è media e deviazione standard degli stipendi per ogni categoria di strutturati? --

select posizione, avg (stipendio) as media, stddev(stipendio) as deviazione_standard
from Persona    
group by posizione;

-- 2. --
-- Quali sono i ricercatori (tutti gli attributi) con uno stipendio superiore alla media della loro categoria? --

select p.nome, p.cognome, p.id, p.posizione, p.stipendio
from Persona p
where p.posizione = 'Ricercatore' 
    and p.stipendio > (
        select avg (stipendio)
        from Persona
        where posizione = p.posizione
    );

-- 3. --
-- Per ogni categoria di strutturati, quante sono le persone con uno stipendio che differisce di al massimo una deviazione standard dalla media della loro categoria? --

select posizione count (*) as Conteggio
from Persona p
where p.stipendio >= (
    select avg (stipendio) - stddev(stipendio)
    from Persona
    where posizione = p.posizione
);

-- 4. --
-- Chi sono gli strutturati che hanno lavorato almeno 20 ore complessive in attività progettuali? 
-- Restituire tutti i loro dati e il numero di ore lavorate. --

select p.id, p.nome, p.cognome, p.posizione, p.stipendio, sum(oreDurata) as ore_lavorate
from Persona p
join AttivitaProgetto ap on p.id = ap.persona
where p.posizione in ('Ricercatore', 'Professore Ordinario', 'Professore Associato')
group by p.id, p.nome, p.cognome, p.posizione, p.stipendio
having sum(ap.oreDurata) >= 20;

-- 5. --
-- Quali sono i progetti la cui durata è superiore alla media delle durate di tutti i progetti?--
-- Restituire nome dei progetti e loro durata in giorni. --

select p.nome, p.fine - p.inizio as durata
from Progetto p
where p.fine - p.inizio > (
    select avg(fine - inizio)
    from Progetto
);

-- 6. --
-- Quali sono i progetti terminati in data odierna che hanno avuto attività di tipo “Dimostrazione”? -- 
-- Restituire nome di ogni progetto e il numero complessivo delle ore dedicate a tali attività nel progetto. --

select p.nome as progetto, sum(ap.oreDurata) as durata
from Progetto p
join AttivitaProgetto ap on p.id = ap.progetto
where p.fine = (select max(fine) from Progetto) and ap.tipo = 'Dimostrazione'
group by p.nome;

-- 7. --
-- Quali sono i professori ordinari che hanno fatto più assenze per malattia del numero di assenze medio per malattia --
-- dei professori associati? Restituire id, nome e cognome del professore e il numero di giorni di assenza per malattia. --

select p.id, p.nome, p.cognome, sum(a.giorno) as totale_assenza
from Persona p
join Assenza a on p.id = a.persona
where p.posizione = 'Professore Ordinario' and a.tipo = 'Malattia'
group by p.id, p.nome, p.cognome
having sum(a.giorno) > (
    select avg(tz.totale_assenza)
    from (
        select sum(az.giorno) as totale_assenza
        from Persona pz
        join Assenza az on pz.id = az.persona
        where pz.posizione = 'Professore Associato' and az.tipo = 'Malattia'
        group by pz.id
    ) tz
);













