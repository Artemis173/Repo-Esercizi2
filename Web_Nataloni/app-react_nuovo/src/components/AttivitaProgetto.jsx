import React, { useEffect, useState } from 'react';
import { Container, Table, Button } from 'react-bootstrap';
import { Link } from 'react-router-dom';
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
    <Container className="mt-4" style={{ fontFamily: 'Arial' }}>
    <h1 className="text-center" style={{ color: 'red' }}>Attività Progettuali</h1>
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
      <div className="text-center mt-4">
        <Button variant="primary">
          <Link to="/" style={{ textDecoration: 'none', color: 'white' }}>
            Torna alla Home
          </Link>
        </Button>
      </div>
    </Container>
  );
};

export default AttivitaProgetto;