import React, { useEffect, useState } from 'react';
import { Container, Table, Button } from 'react-bootstrap';
import { Link } from 'react-router-dom';
import { fetchProgetto } from '../api';

const Progetto = () => {
  const [Progetto, setProgetto] = useState([]);

  useEffect(() => {
    const getProgetto = async () => {
      const data = await fetchProgetto();
      setProgetto(data);
    };
    getProgetto();
  }, []);

  return (
    <Container className="mt-4" style={{ fontFamily: 'Arial' }}>
    <h1 className="text-center" style={{ color: 'red' }}>Progetti</h1>
      <Table striped bordered hover>
        <thead>
          <tr>
            <th>ID</th>
            <th>Nome</th>
            <th>Inizio</th>
            <th>Fine</th>
            <th>Budget</th>
          </tr>
        </thead>
        <tbody>
          {Progetto.map(Progetto => (
            <tr key={Progetto.id}>
              <td>{Progetto.id}</td>
              <td>{Progetto.nome}</td>
              <td>{Progetto.inizio}</td>
              <td>{Progetto.fine}</td>
              <td>{Progetto.budget}</td>
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

export default Progetto;