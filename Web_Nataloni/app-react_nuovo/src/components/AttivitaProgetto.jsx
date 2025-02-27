import React, { useEffect, useState } from 'react';
import { Container, Table } from 'react-bootstrap';
import { fetchAttivitaProgetto } from '../api';

const AttivitaProgetto = () => {
  const [AttivitaProgetto, setAttivitaProgetto] = useState([]);

  useEffect(() => {
    const getAttivitaProgetto = async () => {
      const data = await fetchAttivitaProgetto();
      setAttivitaProgetto(data);
    };
    getAttivitaProgetto();
  }, []);

  return (
    <Container className="mt-4">
      <h1>Attività Progettuali</h1>
      <Table striped bordered hover>
        <thead>
          <tr>
            <th>ID</th>
            <th>Persona</th>
            <th>Progetto</th>
            <th>WP</th>
            <th>Giorno</th>
            <th>Tipo</th>
            <th>oreDurata</th>
          </tr>
        </thead>
        <tbody>
          {AttivitaProgetto.map(AttivitaProgetto => (
            <tr key={AttivitaProgetto.id}>
              <td>{AttivitaProgetto.id}</td>
              <td>{AttivitaProgetto.persona}</td>
              <td>{AttivitaProgetto.progetto}</td>
              <td>{AttivitaProgetto.wp}</td>
              <td>{AttivitaProgetto.giorno}</td>
              <td>{AttivitaProgetto.tipo}</td>
              <td>{AttivitaProgetto.oreDurata}</td>
            </tr>
          ))}
        </tbody>
      </Table>
    </Container>
  );
};

export default AttivitaProgetto;