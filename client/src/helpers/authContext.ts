import { createContext } from "react";

interface states {
  token: string;
  setToken: (value: any) => void;
  refreshToken: string;
  setRefreshToken: (value: any) => void;
  user: any;
  setUser: (value: any) => void;
  expiry: number;
}

const initialStates: states = {
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
