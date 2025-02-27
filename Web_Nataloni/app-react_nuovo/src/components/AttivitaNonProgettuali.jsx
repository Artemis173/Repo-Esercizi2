import React, { useEffect, useState } from 'react';
import { Container, Table } from 'react-bootstrap';
import { fetchAttivitaNonProgettuale } from '../api';

const AttivitaNonProgettuale = () => {
  const [AttivitaNonProgettuale, setAttivitaNonProgettuale] = useState([]);

  useEffect(() => {
    const getAttivitaNonProgettuale = async () => {
      const data = await fetchAttivitaNonProgettuale();
      setAttivitaNonProgettuale(data);
    };
    getAttivitaNonProgettuale();
  }, []);

  return (
    <Container className="mt-4">
      <h1>Attività non Progettuali</h1>
      <Table striped bordered hover>
        <thead>
          <tr>
            <th>ID</th>
            <th>Persona</th>
            <th>Tipo</th>
            <th>Giorno</th>
            <th>oreDurata</th>
          </tr>
        </thead>
        <tbody>
          {AttivitaNonProgettuale.map(AttivitaNonProgettuale => (
            <tr key={AttivitaNonProgettuale.id}>
              <td>{AttivitaNonProgettuale.id}</td>
              <td>{AttivitaNonProgettuale.persona}</td>
              <td>{AttivitaNonProgettuale.giorno}</td>
              <td>{AttivitaNonProgettuale.tipo}</td>
              <td>{AttivitaNonProgettuale.oreDurata}</td>
            </tr>
          ))}
        </tbody>
      </Table>
    </Container>
  );
};

export default AttivitaNonProgettuale;