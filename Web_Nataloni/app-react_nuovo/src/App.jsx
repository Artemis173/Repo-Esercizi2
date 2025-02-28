import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './components/Home';
import Persona from './components/Persone';
import Progetto from './components/Progetti';
import WP from './components/WP';
import AttivitaProgetto from './components/AttivitaProgetto';
import AttivitaNonProgettuale from './components/AttivitaNonProgettuali';
import Assenze from './components/Assenze';

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/Persona" element={<Persona />} />
        <Route path="/Progetto" element={<Progetto />} />
        <Route path="/WP" element={<WP />} />
        <Route path="/AttivitaProgetto" element={<AttivitaProgetto />} />
        <Route path="/AttivitaNonProgettuali" element={<AttivitaNonProgettuale />} />
        <Route path="/Assenze" element={<Assenze />} />
        </Routes>
    </Router>
  );
};

export default App;