import React, { useEffect, useState } from 'react';
import { Container, Table, Button } from 'react-bootstrap';
import { Link } from 'react-router-dom';
import { fetchAssenze } from '../api';

const Assenze = () => {
  const [Assenze, setAssenze] = useState([]);

  useEffect(() => {
    const getAssenze = async () => {
      const data = await fetchAssenze();
      setAssenze(data);
    };
    getAssenze();
  }, []);

  return (
    <Container className="mt-4" style={{ fontFamily: 'Arial' }}>
    <h1 className="text-center" style={{ color: 'red' }}>Assenze</h1>
      <Table striped bordered hover>
        <thead>
          <tr>
            <th>ID</th>
            <th>Persona</th>
            <th>Tipo</th>
            <th>Giorno</th>
          </tr>
        </thead>
        <tbody>
          {Assenze.map(Assenze => (
            <tr key={Assenze.id}>
              <td>{Assenze.id}</td>
              <td>{Assenze.persona}</td>
              <td>{Assenze.giorno}</td>
              <td>{Assenze.tipo}</td>
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

export default Assenze;