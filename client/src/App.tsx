import React from "react";

import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Flights from "./pages/Flights";
import SearchPage from "./pages/Search";
import Home from "./pages/Home";
import LoginPage from "./pages/Login";

function App() {
  return (
    <Router>
      <Routes>
        <Route index element={<Home />} />
        <Route element={<Flights />} path="/flights" />
        <Route element={<SearchPage />} path="/search" />
        <Route element={<LoginPage />} path='/login' />
      </Routes>
    </Router>
  );
}

export default App;
