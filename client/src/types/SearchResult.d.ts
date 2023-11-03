interface AirportInfo {
  airport_info_url: string;
  city: string;
  code: string;
  code_iata: string;
  code_icao: string;
  name: string;
  timezone: string;
}

interface AirlineSearchResult {
  fa_flight_id: string;
  operator: string;
  codeshares_iata: string[];
  ident_iata: string;
  origin: AirportInfo;
  destination: AirportInfo;
  scheduled_on: string;
  scheduled_off: string;
  status: "Scheduled" | "Arrived / Gate Arrival";
  arrival_delay: number;
  aircraft_type: string;
}

export default AirlineSearchResult;
