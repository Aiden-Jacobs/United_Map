from datetime import timedelta

class Flight_():
    """Flight_
    This class represents a flight in an airline schedule.

    Attributes:
        departureAirport (str): The 3-letter code for the airport where the flight departs.
        arrivalAirport (str): The 3-letter code for the airport where the flight arrives.
        departureTime (datetime.datetime): The scheduled departure time for the flight.
        flightTime (datetime.timedelta): The scheduled duration of the flight.
        arrivalTime (datetime.datetime): The scheduled arrival time for the flight, calculated as the sum of departureTime and flightTime.
        flightNumber (str): The flight number for the flight.
        available_JOY (list): A list of integers representing the number of JOY class seats available in the aircraft for this flight.
        SAlisted_JOY (list): A list of integers representing the number of JOY class seats that have been assigned to standby passengers for this flight.
    """
    def __init__(self, departureAirport,arrivalAirport,departureTime,flightTime):
        self.departureAirport = departureAirport
        self.arrivalAirport = arrivalAirport
        self.flightTime = timedelta(seconds=flightTime)
        self.departureTime = departureTime
        self.arrivalTime = departureTime + timedelta(seconds = flightTime)
        #add init args
        self.flightNumber = "UA5676"
        self.available_JOY = [0,0,0]
        self.SAlisted_JOY = [0,0,0]
    def getDepartureAirport(self):
        return(self.departureAirport)
    def getArrivalAirport(self):
        return(self.arrivalAirport)
    def getDepartureTime(self):
        return(self.departureTime)
    def GetFlightTime(self):
        return(self.flightTime)
    def GetArrivalTime(self):
        return(self.arrivalTime)
    def __repr__(self):
        return(str(self.departureAirport)+"->"+str(self.arrivalAirport))
        return(str(self.departureAirport)+"->"+str(self.arrivalAirport)+"\nFlight Time "+str(self.flightTime)+"\nDeparture Time "+str(self.departureTime)+" Arrival Time "+str(self.arrivalTime)+"\n")
