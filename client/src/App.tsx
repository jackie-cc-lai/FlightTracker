import React, { useState } from "react";

import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Flights from "./pages/Flights";
import SearchPage from "./pages/Search";
import LoginPage from "./pages/Login";
import AuthContext from "./helpers/authContext";
import FlightDetails from "./pages/Details";

function App() {
  const [token, setToken] = useState(localStorage.getItem("token"));
  const [user, setUser] = useState(null);
  const [refreshToken, setRefreshToken] = useState(null);

  return (
    <AuthContext.Provider
      value={{
        token,
        setToken,
        user,
        setUser,
        refreshToken,
        setRefreshToken,
        expiry: 500,
      }}
    >
      <Router>
        <Routes>
          <Route index element={<Flights />} />
          <Route element={<FlightDetails />} path="/details/:id" />
          <Route element={<Flights />} path="/flights" />
          <Route element={<SearchPage />} path="/search" />
          <Route element={<LoginPage />} path="/login" />
        </Routes>
      </Router>
    </AuthContext.Provider>
  );
}

export default App;
