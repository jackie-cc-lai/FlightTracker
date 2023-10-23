interface AirlineSearchResult {
  id: string;
  flightNumber: string;
  origin: string;
  destination: string;
  departureDate: string;
  arrivalDate: string;
  hasDeparted: boolean;
  hasArrived: boolean;
  hasDelay: boolean;
  delay?: number;
  planeType: string;
}

export default AirlineSearchResult;
