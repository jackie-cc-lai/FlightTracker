import React, { useState } from "react";

import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Flights from "./pages/Flights";
import SearchPage from "./pages/Search";
import Home from "./pages/Home";
import LoginPage from "./pages/Login";
import AuthContext from "./helpers/authContext";

function App() {
  const [token, setToken] = useState(null);
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
          <Route index element={<Home />} />
          <Route element={<Flights />} path="/flights" />
          <Route element={<SearchPage />} path="/search" />
          <Route element={<LoginPage />} path="/login" />
        </Routes>
      </Router>
    </AuthContext.Provider>
  );
}

export default App;
