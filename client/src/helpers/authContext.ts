import { createContext } from "react";

const initialStates = {
  token: null,
  setToken: (val: any) => {},
  refreshToken: null,
  setRefreshToken: (val: any) => {},
  user: null,
  setUser: (val: any) => {},
  expiry: 900,
};

const AuthContext = createContext(initialStates);

export default AuthContext;
