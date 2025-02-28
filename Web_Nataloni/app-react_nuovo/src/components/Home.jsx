import React from 'react';
import { Container, Card, Button } from 'react-bootstrap';
import { Link } from 'react-router-dom';

const Home = () => {
  return (
    <Container className="mt-4 d-flex justify-content-center">
      <Card
        className="text-center p-4"
        style={{
          borderRadius: '15px',
          boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)',
          background: 'linear-gradient(135deg, #f6d365 0%, #fda085 100%)',
          border: '2px solid #ddd',
          width: '100%',
          maxWidth: '600px'
        }}
      >
        <Card.Body>
          <Card.Title className="display-4">Benvenuto al Portale dell'Università</Card.Title>
          <Card.Text className="mt-3">
            L'accesso a questo portale permette di visualizzare le informazioni sui docenti ed i progetti universitari.
            Utilizza il menu di navigazione per esplorare le sezioni.
          </Card.Text>
          <div className="d-flex flex-column align-items-center gap-2">
            <Button variant="primary" className="w-75">
              <Link to="/Persona" style={{ textDecoration: 'none', color: 'white' }}>
                Visualizza il Personale
              </Link>
            </Button>
            <Button variant="secondary" className="w-75">
              <Link to="/Progetto" style={{ textDecoration: 'none', color: 'white' }}>
                Esplora i Progetti
              </Link>
            </Button>
            <Button variant="success" className="w-75">
              <Link to="/WP" style={{ textDecoration: 'none', color: 'white' }}>
                Esplora i Work Project
              </Link>
            </Button>
            <Button variant="danger" className="w-75">
              <Link to="/AttivitaProgetto" style={{ textDecoration: 'none', color: 'white' }}>
                Esplora le Attività Progettuali
              </Link>
            </Button>
            <Button variant="warning" className="w-75">
              <Link to="/AttivitaNonProgettuali" style={{ textDecoration: 'none', color: 'black' }}>
              Esplora le Attività non Progettuali
              </Link>
            </Button>
            <Button variant="info" className="w-75">
              <Link to="/Assenze" style={{ textDecoration: 'none', color: 'white' }}>
                Registro Assenze
              </Link>
            </Button>
          </div>
        </Card.Body>
      </Card>
    </Container>
  );
};

export default Home;
