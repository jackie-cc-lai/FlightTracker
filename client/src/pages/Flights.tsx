import "../App.css";
import Page from "../components/Page";
import navlinks from "../constants/PageConstants";

function Flights() {
  const activePage = navlinks.find((link) => link.id === "FLIGHTS");
  return (
    <Page active={activePage?.id}>
      <div>Flights</div>
    </Page>
  );
}

export default Flights;
