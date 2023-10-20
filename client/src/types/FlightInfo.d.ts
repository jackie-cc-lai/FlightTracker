interface FlightInfo {
  id: string;
  flightNumber: string;
  departureICAO: string;
  arrivalICAO: string;
  departureTerminal: string;
  arrivalTerminal: string;
  scheduledDepartureTime: Date;
  scheduledArrivalTime: Date;
  estimatedDepartureTime: Date;
  estimatedArrivalTime: Date;
  delay: number;
}

export default FlightInfo;
