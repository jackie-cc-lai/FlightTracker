import React, { useContext, useState } from "react";
import dayjs from "dayjs";

import Page from "../components/Page";
import navlinks from "../constants/PageConstants";
import Table from "../components/Table";

import AirlineSearchResult from "../types/SearchResult";
import Sidebar from "../components/Sidebar";
import api from "../helpers/api";
import headings from "../constants/SearchTableHeader";
import AuthContext from "../helpers/authContext";

interface Props {
  flight: AirlineSearchResult;
  onClose: () => void;
  saveFlight: () => void;
}
function SearchSidebar({ flight, onClose, saveFlight }: Props) {
  return (
    <Sidebar onClose={onClose}>
      <div className="text-lg font-bold">Flight: {flight.ident_iata}</div>
      <div className="info py-4">
        <div className="text-left py-2">
          <span>Origin: </span>
          <span>{flight.origin.city}</span>
        </div>
        <div className="text-left py-2">
          <span>Destination: </span>
          <span>{flight.destination.city}</span>
        </div>
        <div className="text-left py-2">
          <span>Codeshares: </span>
          <span>
            <ul>
              {flight.codeshares_iata.map((iata) => (
                <li>{iata}</li>
              ))}
            </ul>
          </span>
        </div>
        <div className="text-left py-2">
          <span>Scheduled Departure Time: </span>
          <span>
            {dayjs(flight.scheduled_off).format("DD/MM/YYYY hh:mm a")}
          </span>
        </div>
        <div className="text-left py-2">
          <span>Scheduled Arrival Time: </span>
          <span>{dayjs(flight.scheduled_on).format("DD/MM/YYYY hh:mm a")}</span>
        </div>
        <div className="text-left py-2" onClick={saveFlight}>
          <button className="rounded-md py-2 px-4 bg-cyan-300	">
            Save Flight
          </button>
        </div>
      </div>
    </Sidebar>
  );
}

function SearchPage() {
  const { token } = useContext(AuthContext);
  const [searchTable, setSearchTable] = useState<{
    headings: string[];
    data: { key: string; data: string[] }[];
  }>();
  const [searchResults, setSearchResults] = useState<AirlineSearchResult[]>([]);
  const [searchString, setSearchString] = useState("");
  const [openSidebar, setOpenSidebar] = useState(false);
  const [selectedFlight, setSelectedFlight] = useState<AirlineSearchResult>();
  const activePage = navlinks.find((link) => link.id === "SEARCH");
  const handleChange = (e: any) => {
    setSearchString(e.target.value);
  };

  const handleSubmit = async (e: any) => {
    e.preventDefault();
    const searchResponse: { flights: AirlineSearchResult[] } =
      await api.getFlights(searchString, token);
    setSearchResults(searchResponse.flights);
    const data = searchResponse.flights.map((results) => ({
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

  const selectFlight = (flightId: string) => {
    const flight = searchResults?.find((d) => d.fa_flight_id === flightId);
    setSelectedFlight(flight);
    setOpenSidebar(true);
  };

  const saveFlight = async () => {
    const response = await api.saveFlight(selectedFlight, token);
    if (response.status !== 201) {
      console.error("cannot save flight");
    }
  };

  return (
    <Page active={activePage?.id}>
      <div className="mb-10 py-10">
        <form onSubmit={handleSubmit}>
          <input
            type="string"
            className="px-4 py-4 border-2 w-full rounded-md focus:outline-indigo-500"
            onChange={handleChange}
          />
        </form>
      </div>
      {searchTable && (
        <Table
          headings={searchTable.headings}
          data={searchTable.data}
          onClick={selectFlight}
        />
      )}
      {openSidebar && selectedFlight && (
        <SearchSidebar
          onClose={() => {
            setOpenSidebar(false);
            setSelectedFlight(undefined);
          }}
          saveFlight={() => {
            saveFlight();
          }}
          flight={selectedFlight}
        />
      )}
    </Page>
  );
}

export default SearchPage;
