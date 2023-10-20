import React, { useState } from "react";
import Page from "../components/Page";
import navlinks from "../constants/PageConstants";

function SearchPage() {
  const [searchResults, setSearchResults] = useState([]);
  const [searchString, setSearchString] = useState("");
  const activePage = navlinks.find((link) => link.id === "SEARCH");

  const handleChange = (e: any) => {
    setSearchString(e.target.value);
  };

  const handleSubmit = async (e: any) => {
    e.preventDefault();
    console.log(searchString);
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
      <div>Search page</div>
    </Page>
  );
}

export default SearchPage;
