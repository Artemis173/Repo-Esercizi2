import React from 'react';
import { Navbar, Nav, Container } from 'react-bootstrap';
import { Link } from 'react-router-dom';

const CustomNavbar = () => {
  return (
    <Navbar bg="light" expand="lg">
      <Container>
        <Navbar.Brand as={Link} to="/">My App</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">
            <Nav.Link as={Link} to="/">Home</Nav.Link>
            <Nav.Link as={Link} to="/Persona">Persone</Nav.Link>
            <Nav.Link as={Link} to="/Progetto">Progetti</Nav.Link>
            <Nav.Link as={Link} to="/WP">WP</Nav.Link>
            <Nav.Link as={Link} to="/AttivitaProgetto">Attivita Progetti</Nav.Link>
            <Nav.Link as={Link} to="/AttivitaNonProgettuali">Attivita non Progettuali</Nav.Link>
            <Nav.Link as={Link} to="/WP">WP</Nav.Link>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
};

export default CustomNavbar;