import { useContext, useEffect, useState } from "react";
import dayjs from "dayjs";

import "../App.css";
import Page from "../components/Page";
import api from "../helpers/api";
import AuthContext from "../helpers/authContext";

import AirlineSearchResult from "../types/SearchResult";
import { useParams } from "react-router-dom";

function FlightDetails() {
  const { token } = useContext(AuthContext);
  const [flight, setUserFlight] = useState<AirlineSearchResult>();

  const { id } = useParams();

  useEffect(() => {
    getFlights();
  }, []);

  const getFlights = async () => {
    const response = await api.getFlightById(id, token);
    setUserFlight(response);
  };

  return (
    <Page>
      {flight && (
        <div>
          <div className="text-lg font-bold">Flight: {flight.ident_iata}</div>
          <div className="info py-4">
            <div className="text-left py-2">
              <span>Status: </span>
              <span>{flight.status}</span>
            </div>
            {flight.status !== "Arrived / Gate Arrival" && (
              <div className="text-left py-2">
                <span>Progress: </span>
                <span>{flight.progress_percent}%</span>
              </div>
            )}
            <div className="text-left py-2">
              <span>Origin: </span>
              <span>{flight.origin.city}</span>
            </div>
            <div className="text-left py-2">
              <span>Destination: </span>
              <span>{flight.destination.city}</span>
            </div>
            <div className="text-left py-2">
              <span>Codeshare Flights: </span>
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
              <span>
                {dayjs(flight.scheduled_on).format("DD/MM/YYYY hh:mm a")}
              </span>
            </div>
            <div className="">
              <span>Route: </span>
              <span>{flight.route}</span>
            </div>
            <div className="">
              <span>Distance: </span>
              <span>{flight.route_distance}</span>
            </div>
          </div>
        </div>
      )}
    </Page>
  );
}

export default FlightDetails;
