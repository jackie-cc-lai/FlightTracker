interface AirlineSearchResult {
  id: string;
  flightNumber: string;
  departureDate: string;
  arrivalDate: string;
  hasDeparted: boolean;
  hasArrived: boolean;
  hasDelay: boolean;
  delay?: number;
  planeType: string;
}

export default AirlineSearchResult;
