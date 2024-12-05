select codice, comp
from Volo
where durataMinuti > 180;

select distinct comp
from Volo
where  durataMinuti > 180;

select codice, comp
from ArrPart
where partenza = 'CIA';

select codice, comp
from ArrPart
where arrivo = 'FCO';

select codice, comp
from ArrPart
where partenza = 'FCO' and arrivo = 'JFK';

select comp
from ArrPart
where partenza = 'FCO' and arrivo = 'JFK';

select DISTINCT v.comp
from Volo v
join ArrPart ap on v.codice = ap.codice
join LuogoAeroporto la1 on ap.arrivo = la1.aeroporto
join LuogoAeroporto la2 on ap.partenza = la2.aeroporto
where la1.citta = 'New York' and la2.citta = 'Roma';

select distinct a.partenza as codice, ae.nome, la.citta
from ArrPart a, aereoporto ae, luogoAeroporto la
where a.partenza = ae.codice and ae.codice = la.aereoporto and a.comp = 'MagicFly';

select v.codice, v.comp, laPart.nome AS aeroportoPartenza, laArr.nome AS aeroportoArrivo
from Volo v
join ArrPart ap on v.codice = ap.codice
join LuogoAeroporto laPart on ap.partenza = laPart.aeroporto
join LuogoAeroporto laArr on ap.arrivo = laArr.aeroporto
where laPart.citta = 'Roma' and laArr.citta = 'New York';
