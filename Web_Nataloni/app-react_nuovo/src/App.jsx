import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import CustomNavbar from './components/Navbar';
import Home from './components/Home';
import Persona from './components/Persone';
import Progetto from './components/Progetti';
import WP from './components/WP';
import AttivitaProgetto from './components/AttivitaProgetto';
import AttivitaNonProgettuale from './components/AttivitaNonProgettuali';

const App = () => {
  return (
    <Router>
      <CustomNavbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/Persona" element={<Persona />} />
        <Route path="/Progetto" element={<Progetto />} />
        <Route path="/WP" element={<WP />} />
        <Route path="/AttivitaProgetto" element={<AttivitaProgetto />} />
        <Route path="/AttivitaNonProgettuali" element={<AttivitaNonProgettuale />} />
      </Routes>
    </Router>
  );
};

export default App;