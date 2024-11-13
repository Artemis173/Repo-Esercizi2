select a.codice, a.nome, count(c.nome) as num_compagnie
from aeroporto a, compagnia c, arrPart ap
where (a.codice = ap.arrivo or a.codice = ap.partenza) and ap.comp = c.nome
group by a.codice;

select a.codice, count(v.codice) as num_aeroplani
from aeroporto a, Volo v , arrPart ap
where a.codice = 'HTR' and (a.codice = ap.arrivo or a.codice = ap.partenza) and ap.codice = v.codice and v.durataMinuti > 100
group by a.codice;

select l.nazione, count(l.aeroporto) as num_aeroporti
from luogoAeroporto l, arrPart ap, compagnia c
where (l.aeroporto = ap.arrivo or l.aeroporto = ap.partenza) and ap.comp = c.nome and c.nome = 'Apitalia'
group by l.nazione;

select cast(avg(v.durataMinuti) as decimal(10,2)) as media, max(v.durataMinuti) as massimo, min(v.durataMinuti) as minimo
from volo v, compagnia c
where v.comp = c.nome and c.nome = 'MagicFly';

select a.codice, a.nome, min(c.annoFondaz)
from aeroporto a, arrPart ap, compagnia c
where (a.codice = ap.arrivo or a.codice = ap.partenza) and ap.comp = c.nome
group by a.codice;

select l.nazione, count(distinct l2.nazione) as num_nazioni
from luogoAeroporto l, luogoAeroporto l2, arrPart ap
where l.aeroporto = ap.arrivo and l2.aeroporto = ap.partenza
group by l.nazione;

select a.codice, a.nome, cast(avg(v.durataMinuti) as decimal(10,2)) as media
from aeroporto a, arrPart ap, volo v
where (a.codice = ap.arrivo or a.codice = ap.partenza) and ap.codice = v.codice
group by a.codice;

select c.nome, sum(v.durataMinuti) as totale
from compagnia c, volo v
where c.nome = v.comp and c.annoFondaz >= 1950
group by c.nome;

select a.codice, a.nome
from aeroporto a, compagnia c, arrPart ap
where (a.codice = ap.arrivo or a.codice = ap.partenza) and ap.comp = c.nome
group by a.codice
having count(distinct c.nome) = 2; 

select l.citta
from luogoAeroporto l, aeroporto a
where a.codice = l.aeroporto
group by l.citta
having count(a.codice) >= 2;
select c.nome
from compagnia c, volo v
where c.nome = v.comp
group by c.nome
having avg(v.durataMinuti) > 6*60;

select c.nome
from compagnia c, volo v
where c.nome = v.comp
group by c.nome
having min(v.durataMinuti) > 100;