import React, { useState } from "react";
import Page from "../components/Page";
import navlinks from "../constants/PageConstants";
import mockSearchResults from "../mock/mockSearch";
import Table from "../components/Table";

const headings = [
  "Flight Number",
  "Departure Date",
  "Estimated Departure Time",
  "Actual Departure Time",
  "Arrival Date",
  "Estimated Arrival Date",
  "Actual Arrival Date",
  "Delays",
  "Plane Type",
];

function SearchPage() {
  const [searchResults, setSearchResults] = useState<{
    headings: string[];
    data: any[];
  }>();
  const [searchString, setSearchString] = useState("");
  const activePage = navlinks.find((link) => link.id === "SEARCH");
  const handleChange = (e: any) => {
    setSearchString(e.target.value);
  };

  const handleSubmit = async (e: any) => {
    e.preventDefault();
    console.log(searchString);
    const headings = Object.keys(mockSearchResults[0]);
    const data = mockSearchResults.map((results) => {
      return Object.values(results);
    });
    console.log(data);
    setSearchResults({
      headings,
      data,
    });
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
      {searchResults && (
        <Table headings={searchResults.headings} data={searchResults.data} />
      )}
    </Page>
  );
}

export default SearchPage;
