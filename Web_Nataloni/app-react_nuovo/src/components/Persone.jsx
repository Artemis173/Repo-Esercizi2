import React, { useEffect, useState } from 'react';
import { Container, Table, Button } from 'react-bootstrap';
import { Link } from 'react-router-dom';
import { fetchPersona } from '../api';

const generateRandomEmail = () => {
  const domains = ['gmail.com', 'libero.it', 'hotmail.com'];
  const name = Math.random().toString(36).substring(2, 8);
  const domain = domains[Math.floor(Math.random() * domains.length)];
  return `${name}@${domain}`;
};

const generateRandomUsername = () => {
  return `user_${Math.random().toString(36).substring(2, 8)}`;
};

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
    <Container className="mt-4" style={{ fontFamily: 'Arial' }}>
    <h1 className="text-center" style={{ color: 'red' }}>Docenti</h1>
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
              <td>{generateRandomEmail()}</td>
              <td>{generateRandomUsername()}</td>
              <td>{Persona.posizione}</td>
              <td>{Persona.stipendio}</td>
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

export default Persona;