import axios from "axios";

const getFlights = async (search: string) => {
  const url = process.env.REACT_APP_SERVER_URL;
  try {
    const response = await axios.get(`${url}/searchFlights?flightId=${search}`);
    return response.data;
  } catch (err) {
    console.error("cannot retrieve data from server", err);
    return {};
  }
};

const login = async (email: string) => {
  const url = process.env.REACT_APP_SERVER_URL;
  try {
    const response = await axios.post(`${url}/login`, {
      email,
    });
    return response.data;
  } catch (err) {
    console.error(err);
  }
};

export default {
  getFlights,
  login,
};
