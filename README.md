# United_Map

Requienments 
    (1) Flask (pip install flask)
    (2) Pandas (pip install pandas)


United Map

    """Route_Manager
    This class serves as a management wrapper for the Route Class. It allows for easy
    sorting and filtering of routes, making it easier to display routes to a user based on
    a variety of criteria.
Functions:
    sortST - sorts with stops and time
    getRoutes - gets the routes
    sortByStops - sorts by stops
    filterByStops - filters by stops
    filterLessThanNStops - filters less than n stops
    sortByTime - sorts by time
    """

    """Route_
    the Route_ class is used to create a route, and then keep track of the route. 
    It takes in a list of flights, and then calculates the number of flights and 
    the route time. It has functions to get the list, get the value (number of flights
    and the route time), get a flight by index, get the number of flights, and get
    the route time. You can print out a route by printing the object.
    Functions:
        getList - Returns the list of flights in the route. 
        getValue - Returns a tuple containing the number of flights and the route time. 
        getFlightByIndex - Returns the flight at the given index. 
        getNumFlights - Returns the number of flights in the route. 
        getRouteTime - Returns the route time. 
    """
    
    """Route Finder
    This class is used to find routes for a particular day. 
    It creates an instance of the Info_for_Day class, which contains information about all flights for that day. 
    This class can then use a series of functions to create possible routes for the day and return
    the possible routes, so that the user may select from them. 
    Functions:
        -GetDepartureAirports: returns list of airports in self.DayInfo that have departures
        -GetFoundRoutes: returns self.FoundRoutes
        -FindRoute: creates a list of Route_ objects and sets self.FoundRoutes to this list
        -GenerateRoutes: generates all possible routes from Start to End, given StartTime and a list of already searched airports
        -CheckValidStartEnd: checks if Start and End are the same, or if there are flights going from Start to End on that day 
        -GetNeighbors: returns a list of Flight_ objects which depart from Start after given time
        -FindFlightsFrom: returns list of Flight_ objects which depart from Start
        -FindFlightsTo: returns list of Flight_ objects which have Dest as their destination
    """
    
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
    Functions:
        getDepartureAirport- gets the departureAirport
        getArrivalAirport- gets the arrivalAirport
        getDepartureTime- gets the departureTime
        GetFlightTime- gets the flightTime
        GetArrivalTime- gets the arrivalTime
    """
    
    
    """INFO_for_Day
    This class stores information about flights departing from and arriving at an airport on a particular date.

    Attributes:
        FlightsFromAP (dict): A dictionary with airports as keys, and lists of flights departing from those airports as values.
        ArrivalsAtAP (dict): A dictionary with airports as keys, and lists of flights arriving at those airports as values.
        date (datetime): The date for which flight information is being stored.
    Functions:
        getDate - returns the date 
        containsApInDp - returns True if the airport is a key in the FlightsFromAP dictionary, False otherwise 
        containsApInArrivals - returns True if the airport is a key in the ArrivalsAtAP dictionary, False otherwise 
        addFlight - adds a flight to both dictionary attributes of the class 
        getFlightsOutOf - returns a list of all flights departing from a specified airport 
        getFlightsTo - returns a list of all flights arriving at a specified airport 
        getFlightsFromTo - returns a list of all flights from one specified airport to another
    """
