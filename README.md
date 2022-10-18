# United_Map
United Map

    """Route_Manager
    This class serves as a management wrapper for the Route Class. It allows for easy
    sorting and filtering of routes, making it easier to display routes to a user based on
    a variety of criteria.
    """

    """Route_
    the Route_ class is used to create a route, and then keep track of the route. 
    It takes in a list of flights, and then calculates the number of flights and 
    the route time. It has functions to get the list, get the value (number of flights
    and the route time), get a flight by index, get the number of flights, and get
    the route time. You can print out a route by printing the object.
    """
    
    """Route Finder
    This class is used to find routes for a particular day. 
    It creates an instance of the Info_for_Day class, which contains information about all flights for that day. 
    This class can then use a series of functions to create possible routes for the day and return
    the possible routes, so that the user may select from them. 
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
    """
    
    
    """INFO_for_Day
    This class stores information about flights departing from and arriving at an airport on a particular date.

    Attributes:
        FlightsFromAP (dict): A dictionary with airports as keys, and lists of flights departing from those airports as values.
        ArrivalsAtAP (dict): A dictionary with airports as keys, and lists of flights arriving at those airports as values.
        date (datetime): The date for which flight information is being stored.
    """
