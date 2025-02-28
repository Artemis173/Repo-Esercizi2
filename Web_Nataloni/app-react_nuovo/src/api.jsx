import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:8080';

export const fetchPersona = async () => {
  try {
    const response = await axios.get(`${API_BASE_URL}/Persona`);
    return response.data;
  } catch (error) {
    console.error('Error fetching users:', error);
    return [];
  }
};

export const fetchProgetto = async () => {
  try {
    const response = await axios.get(`${API_BASE_URL}/Progetto`);
    return response.data;
  } catch (error) {
    console.error('Error fetching projects:', error);
    return [];
  }
};

export const fetchWP = async () => {
  try {
    const response = await axios.get(`${API_BASE_URL}/WP`);
    return response.data;
  } catch (error) {
    console.error('Error fetching wp:', error);
    return [];
  }
};

export const fetchAttivitaProgetto = async () => {
  try {
    const response = await axios.get(`${API_BASE_URL}/AttivitaProgetto`);
    return response.data;
  } catch (error) {
    console.error('Error fetching projectual activities:', error);
    return [];
  }
};

export const fetchAttivitaNonProgettuale = async () => {
  try {
    const response = await axios.get(`${API_BASE_URL}/AttivitaNonProgettuali`);
    return response.data;
  } catch (error) {
    console.error('Error fetching non projectual activities:', error);
    return [];
  }
};

export const fetchAssenze = async () => {
  try {
    const response = await axios.get(`${API_BASE_URL}/Assenze`);
    return response.data;
  } catch (error) {
    console.error('Error fetching absence:', error);
    return [];
  }
};