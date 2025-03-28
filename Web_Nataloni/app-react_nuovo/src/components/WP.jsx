import React, { useEffect, useState } from 'react';
import { Container, Table, Button } from 'react-bootstrap';
import { Link } from 'react-router-dom';
import { fetchWP } from '../api';

const WP = () => {
  const [WP, setWP] = useState([]);

  useEffect(() => {
    const getWP = async () => {
      const data = await fetchWP();
      setWP(data);
    };
    getWP();
  }, []);

  return (
    <Container className="mt-4" style={{ fontFamily: 'Arial' }}>
    <h1 className="text-center" style={{ color: 'red' }}>Work Projects</h1>
      <Table striped bordered hover>
        <thead>
          <tr>
            <th>ID</th>
            <th>Progetto</th>
            <th>Nome</th>
            <th>Inizio</th>
            <th>Fine</th>
          </tr>
        </thead>
        <tbody>
          {WP.map(WP => (
            <tr key={WP.id}>
              <td>{WP.id}</td>
              <td>{WP.progetto}</td>
              <td>{WP.nome}</td>
              <td>{WP.inizio}</td>
              <td>{WP.fine}</td>
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

export default WP;