import axios from "axios";

const getFlights = async (search: string) => {
  const url = process.env.REACT_APP_SERVER_URL;
  console.log(process.env);
  try {
    const response = await axios.get(`${url}/searchFlights?flightId=${search}`);
    return response;
  } catch (err) {
    console.error("cannot retrieve data from server", err);
    return {};
  }
};

export default {
  getFlights,
};
