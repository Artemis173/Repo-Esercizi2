INSERT INTO Gilde (nome, tipo, fondazione) VALUES
('Gilda dei Ladri', 'Ladri', '1500-05-10'),
('Gilda dei Maghi', 'Maghi', '1450-03-20'),
('Gilda dei Mercanti', 'Commercio', '1600-01-15'),
('Gilda dei Guerrieri', 'Militare', '1580-11-05'),
('Gilda degli Avventurieri', 'Avventurieri', '1620-07-01');

INSERT INTO Persona (nome, cognome, ruolo, stipendio, gilda_id) VALUES
('Mario', 'Rossi', 'Guerriero', 1500.00, 1),
('Luigi', 'Verdi', 'Mago', 2000.00, 2),
('Anna', 'Bianchi', 'Curatore', 1800.00, 1),
('Carlo', 'Neri', 'Talker', 1600.00, 2),
('Giulia', 'Gialli', 'Capogilda', 2500.00, 1),
('Marco', 'Ferri', 'Guerriero', 1500.00, 3),
('Sofia', 'Moretti', 'Mago', 2200.00, 4);

INSERT INTO Mercato (nome, tipo, funzione) VALUES
('Mercato dei Ladri', 'Nero', 'Vendita'),
('Mercato dei Maghi', 'Magico', 'Acquisto'),
('Mercato degli Avventurieri', 'Avventuriero', 'Vendita');

INSERT INTO Camere (gilda_id, numero) VALUES
(1, 101),
(2, 202),
(3, 303),
(4, 404),
(5, 505);

INSERT INTO MissioniInterne (gilda_id, tipo, data, ricompensa) VALUES
(1, 'Attività Pubbliche', '2024-05-01', 300.00),
(1, 'Attività di Guardia', '2024-06-15', 150.00),
(2, 'Attività Pubbliche', '2024-07-10', 500.00);

INSERT INTO MissioniEsterne (gilda_id, tipo, data, ricompensa) VALUES
(1, 'Taglia di Caccia', '2024-04-20', 700.00),
(2, 'Pulizia Dungeon', '2024-07-10', 400.00),
(3, 'Taglia di Banditi', '2024-08-15', 600.00);