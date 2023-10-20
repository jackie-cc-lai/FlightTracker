import React from "react";

import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Flights from "./pages/Flights";
import SearchPage from "./pages/Search";
import Home from "./pages/Home";

function App() {
  return (
    <Router>
      <Routes>
        <Route index element={<Home />} />
        <Route element={<Flights />} path="/flights" />
        <Route element={<SearchPage />} path="/search" />
      </Routes>
    </Router>
  );
}

export default App;
