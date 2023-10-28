import React, { useState } from "react";
import dayjs from "dayjs";

import Page from "../components/Page";
import navlinks from "../constants/PageConstants";
import Table from "../components/Table";

import mockSearchResults from "../mock/mockSearch";
import AirlineSearchResult from "../types/SearchResult";
import Sidebar from "../components/Sidebar";
import api from "../helpers/api";

interface Props {
  flight: AirlineSearchResult;
  onClose: () => void;
}
function SearchSidebar({ flight, onClose }: Props) {
  return (
    <Sidebar onClose={onClose}>
      <div className="header">Flight {flight.flightNumber}</div>
      <div className="info">
        <div className="text-left">
          <span>Origin: </span>
          <span>{flight.origin}</span>
        </div>
        <div className="text-left">
          <span>Destination: </span>
          <span>{flight.destination}</span>
        </div>
        <div className="text-left">
          <span>Departure Time: </span>
          <span>
            {dayjs(flight.departureDate).format("DD/MM/YYYY hh:mm a")}
          </span>
        </div>
        <div className="text-left">
          <span>Estimated Arrival Time: </span>
          <span>{dayjs(flight.arrivalDate).format("DD/MM/YYYY hh:mm a")}</span>
        </div>
      </div>
    </Sidebar>
  );
}

function SearchPage() {
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
    console.log(searchString);
    const response1 = await api.getFlights(searchString);
    setSearchResults(mockSearchResults.data);
    const headings = mockSearchResults.headings;
    const data = mockSearchResults.data.map((results) => ({
      key: results.id,
      data: [
        results.flightNumber,
        results.origin,
        results.destination,
        dayjs(results.departureDate).format("DD/MM/YYYY hh:mm a"),
        dayjs(results.arrivalDate).format("DD/MM/YYYY hh:mm a"),
        results.hasDelay ? "Delayed" : "On Time",
        results.planeType,
      ],
    }));
    setSearchTable({
      headings,
      data,
    });
  };

  const selectFlight = (flightId: string) => {
    const flight = searchResults?.find((d) => d.id === flightId);
    setSelectedFlight(flight);
    setOpenSidebar(true);
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
          flight={selectedFlight}
        />
      )}
    </Page>
  );
}

export default SearchPage;
