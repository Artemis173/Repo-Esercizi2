import React, { useEffect, useState } from 'react';
import { Container, Table } from 'react-bootstrap';
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
    <Container className="mt-4">
      <h1>Persone</h1>
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
    </Container>
  );
};

export default WP;