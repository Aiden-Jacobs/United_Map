from datetime import datetime
class INFO_for_Day():
    """INFO_for_Day
    This class stores information about flights departing from and arriving at an airport on a particular date.

    Attributes:
        FlightsFromAP (dict): A dictionary with airports as keys, and lists of flights departing from those airports as values.
        ArrivalsAtAP (dict): A dictionary with airports as keys, and lists of flights arriving at those airports as values.
        date (datetime): The date for which flight information is being stored.
    """
    def __init__(self):
        self.FlightsFromAP = {"SFO":[],
                            "SBP":[],
                            "LAX":[],
                            "MSP":[],
                            "DEN":[],
                            "ORD":[],
                            "ASE":[],
                            "IAH":[],
                            "MSY":[]}
        self.ArrivalsAtAP = {}
        self.date = datetime(2022,10,13,0,0,0) # add get date from data
    def getFlightsOutOf(self,departureAirport):
        if departureAirport in self.FlightsFromAP:
            return(self.FlightsFromAP[departureAirport])
        return([])

    def addFlight(self, flight):
        #add to FlightsFromAP (Departures for airport)
        DptA = flight.getDepartureAirport()
        ArrivalAp = flight.getArrivalAirport()
        if not self.containsApInDp(DptA):
            self.FlightsFromAP[DptA] = [flight]
        else:
            self.FlightsFromAP[DptA].append(flight)
        #add to ArrivalsAtAP (Arrivals At for airport)
        if self.containsApInArrivals(ArrivalAp):
            self.ArrivalsAtAP[ArrivalAp].append(flight)
        else:
            self.ArrivalsAtAP[ArrivalAp] = [flight]

    def getFlightsFromTo(self,departureAirport,arrivalAirport):
        list = self.getFlightsOutOf(departureAirport)
        out = []
        for flight in list:
            if flight.getArrivalAirport() == arrivalAirport:
                out.append(flight)
        return(out)

    def getFlightsTo(self, arrivalAirport):
        #it might be better to make an arrival list when creating
        return(self.ArrivalsAtAP[arrivalAirport])
        pass

    def containsApInDp(self, Ap):
        return(Ap in self.FlightsFromAP)

    def containsApInArrivals(self, Ap):
        return(Ap in self.ArrivalsAtAP)

    def getdepartureAirports(self):
        return(self.FlightsFromAP.keys())

    def getDate(self):
        return(self.date)
        pass
