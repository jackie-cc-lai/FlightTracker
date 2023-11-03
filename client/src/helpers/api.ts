import axios from "axios";

const getFlights = async (search: string, token: string) => {
  const url = process.env.REACT_APP_SERVER_URL;
  try {
    const response = await axios.get(
      `${url}/searchFlights?flightId=${search}`,
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
    return response.data;
  } catch (err) {
    console.error("cannot retrieve data from server", err);
    return {};
  }
};

const login = async ({
  email,
  password,
}: {
  email: string;
  password: string;
}): Promise<{ token: string | null; user: any }> => {
  const url = process.env.REACT_APP_SERVER_URL;
  try {
    const response = await axios.post(`${url}/login`, {
      email,
      password,
    });
    return response.data as { token: string; user: any };
  } catch (err) {
    console.error(err);
    return { token: null, user: null };
  }
};

export default {
  getFlights,
  login,
};
