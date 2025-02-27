import React, { useEffect, useState } from 'react';
import { Container, Table } from 'react-bootstrap';
import { fetchPersona } from '../api';

const Persona = () => {
  const [Persona, setPersona] = useState([]);

  useEffect(() => {
    const getPersona = async () => {
      const data = await fetchPersona();
      setPersona(data);
    };
    getPersona();
  }, []);

  return (
    <Container className="mt-4">
      <h1>Persone</h1>
      <Table striped bordered hover>
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Email</th>
            <th>Username</th>
            <th>Posizione</th>
            <th>Stipendio</th>
          </tr>
        </thead>
        <tbody>
          {Persona.map(Persona => (
            <tr key={Persona.id}>
              <td>{Persona.id}</td>
              <td>{Persona.nome}</td>
              <td>{Persona.email}</td>
              <td>{Persona.username}</td>
              <td>{Persona.posizione}</td>
              <td>{Persona.stipendio}</td>
            </tr>
          ))}
        </tbody>
      </Table>
    </Container>
  );
};

export default Persona;