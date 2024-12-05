
-- COMANDI TERMINALE --

-- docker exec -it postgres_container bash = accedere al root da terminale --
-- psql -U postgres = accedere a postgres da terminale --
-- create table; = creare tabelle --
-- drop table; = cancellare tabelle --
-- alter table; = modificare tabelle --
-- \i  file.sql; = eseguire il file sql --
-- \c = per accedere ai database --
-- \l = Visualizzare  dati di database --
-- \q = per uscire dal database --
-- \d = per visualizzare le tabelle --

-- COMANDI QUERY --

select = ritorna i dati richiesti della tabella a cui si è interessati

select distinct = ritonra i dati richiesti senza ripeterli della tabella a cui si è interessati

select * = ritorna tutti i dati presenti della tabella a cui si è interessati

from =  specifica la tabella da cui si vuole prendere i dati

where =  specifica le condizioni per cui si vuole prendere i dati

    like = usato esclusivamente con where per ricercare uno specifico dato nelle colonne della tabella a cui si è interessati
        es: -- Select all customers that starts with the letter "a": --
            SELECT * FROM Customers
            WHERE CustomerName LIKE 'a%'; -- a% indica che il dato ricercato inizia per 'a'. 
                                        --'%a' indica che il dato ricercato terminasse per 'a' --
                                        -- '%a%' indica che il dato ricercato continene la lettera a --

        es: -- Return all customers from a city that starts with 'L' --
            -- followed by one wildcard character, then 'nd' and then two wildcard characters: --
            SELECT * FROM Customers
            WHERE city LIKE 'L_nd__'; -- L'Underscore (_) indica un singolo carattere. --
                                      -- Può essere qualsiasi carattere o numero ma ne rappresenta uno e soltanto uno --


group by  =  specifica le colonne per cui si vuole raggruppare i dati

having =  specifica le condizioni per cui si vuole raggruppare i dati

order by  =  specifica l'ordine in cui si vuole visualizzare i dati'

limit  =  specifica il numero di righe da visualizzare

join  =   specifica le tabelle da cui si vuole prendere i dati

count(dato) ... as ...  =  conta il numero di righe che soddisfano la condizione
avg(dato) ... as ... = calcola la media dei dati
sum(dato) ... as ... = calcola la somma dei dati
min(dato) ... as ... = calcola il minimo dei dati
max(dato) ... as ... = calcola il massimo dei dati

wildcards  =  caratteri speciali che si utilizzano per ricercare i dati
    % =  indica che il dato ricercato può essere qualsiasi cosa prima o dopo    
    _  =  indica che il dato ricercato è un singolo carattere
