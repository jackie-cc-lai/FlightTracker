import { useContext, useEffect, useState } from "react";
import dayjs from "dayjs";

import "../App.css";
import Page from "../components/Page";
import navlinks from "../constants/PageConstants";
import api from "../helpers/api";
import AuthContext from "../helpers/authContext";
import Table from "../components/Table";

import headings from "../constants/SearchTableHeader";
import { useNavigate } from "react-router-dom";
import AirlineSearchResult from "../types/SearchResult";

function Flights() {
  const { token } = useContext(AuthContext);
  const [userFlights, setUserFlights] = useState([]);
  const [searchTable, setSearchTable] = useState<{
    headings: string[];
    data: { key: string; data: string[] }[];
  }>();
  const activePage = navlinks.find((link) => link.id === "FLIGHTS");
  const navigate = useNavigate();
  useEffect(() => {
    getFlights();
  }, []);

  const getFlights = async () => {
    const response: AirlineSearchResult[] = await api.getUserFlights(token);
    setUserFlights(response);
    const data = response.map((results) => ({
      key: results.fa_flight_id,
      data: [
        results.ident_iata,
        results.operator,
        results.origin.city,
        results.destination.city,
        dayjs(results.scheduled_off).format("DD/MM/YYYY hh:mm a"),
        dayjs(results.scheduled_on).format("DD/MM/YYYY hh:mm a"),
        results.arrival_delay > 0 ? "Delayed" : "On Time",
        results.aircraft_type,
      ],
    }));
    setSearchTable({
      headings,
      data,
    });
  };

  const getDetails = (flightId: string) => {
    const flight = userFlights?.find((d) => d.fa_flight_id === flightId);
    navigate(`/details/${flightId}`);
  };

  return (
    <Page active={activePage?.id}>
      {searchTable && (
        <Table
          headings={searchTable.headings}
          data={searchTable.data}
          onClick={getDetails}
        />
      )}
      <button
        className="border-2 bg-teal-200 p-4 rounded-md  "
        onClick={() => getFlights()}
      >
        Resend request
      </button>
    </Page>
  );
}

export default Flights;
