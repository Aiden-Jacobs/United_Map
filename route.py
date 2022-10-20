from datetime import datetime

class Route_():
    """Route_
    the Route_ class is used to create a route, and then keep track of the route. 
    It takes in a list of flights, and then calculates the number of flights and 
    the route time. It has functions to get the list, get the value (number of flights
    and the route time), get a flight by index, get the number of flights, and get
    the route time. You can print out a route by printing the object.
    """
    def __init__(self, route):
        self.route = route
        self.numFlights = len(self.route)
        self.routeTime = self.getFlightByIndex(self.numFlights-1).GetArrivalTime() - self.getFlightByIndex(0).getDepartureTime()
        pass

    def getList(self):
        return(self.route)

    def getValue(self):
        #print(self.getNumFlights(),self.getRouteTime())
        return(self.getNumFlights(),self.getRouteTime())

    def getFlightByIndex(self, n):
        if n >= 0 and n < self.getNumFlights():
            return(self.route[n])
        print("Invalid index")

    def getNumFlights(self):
        return(self.numFlights)

    def getRouteTime(self):
        return(self.routeTime)

    def __repr__(self):
        if 1 == 1:
            out = []
            for f in self.route:
                out.append(f.getDepartureAirport())
                out.append(f.getArrivalAirport())
            temp = "->".join(out)
            return(str(temp)+": "+str(self.getNumFlights()-1)+" stop, "+str(self.getRouteTime())+" Route Time")

class Route_Finder():
    """Route Finder
        This class is used to find routes for a particular day. 
        It creates an instance of the Info_for_Day class, which contains information about all flights for that day. 
        This class can then use a series of functions to create possible routes for the day and return
        the possible routes, so that the user may select from them. 
    """
    def __init__(self, info):
        self.DayInfo = info # Class INFO_for_Day
        self.FoundRoutes = []
    
    def checkValidStartEnd(self,Start,End):
        if Start == End:
            return(False)
        if self.DayInfo.containsApInDp(Start) == True and self.DayInfo.containsApInArrivals(End) == True:
            return(True)
        return(False)
    
    def getNeighbors(self, Start, time):
        # returns list of Flight_
        out = []
        flightsFromStart = self.DayInfo.getFlightsOutOf(Start)
        for f in flightsFromStart:
            if f.getDepartureTime() > time:
                out.append(f)
        return(out)


    #implement lightest spanning tree
    def generateRoutes(self,Start,End, StartTime, searched):
        """generateRoutes
        This function will generate a list of all possible routes from the given starting airport to the given ending airport.

        Start: the starting airport for the route
        End: the ending airport for the route
        StartTime: the time at which the first flight of the route will depart
        searched: a list of airports which have already been searched; this is used to prevent infinite loops
        """
        get = []
        out = []
        if Start == End:
            return
        if Start not in searched:
            for f in self.getNeighbors(Start, StartTime):
                get.append([f])
            searched.append(Start)

        for r in get:
            if r[len(r)-1].getArrivalAirport() not in searched:
                modSearched = searched.copy()
                airportJustLeft = r[len(r)-1].getDepartureAirport
                modSearched.append(airportJustLeft)
                nextDepartureAirport = r[len(r)-1].getArrivalAirport()
                nextPossibleDepartureTime = r[len(r)-1].GetArrivalTime()
                temp = self.generateRoutes(nextDepartureAirport,End,nextPossibleDepartureTime,modSearched)
                if temp == None:
                    out.append(r)
                    #out
                else:
                    for t in temp:
                        newR = r.copy()
                        for i in range(len(t)):
                            newR.append(t[i])
                        out.append(newR)
                pass
        return(out)

    def findRoute(self,Start,End, StartTime, searched):
        if self.checkValidStartEnd(Start,End) == False:
            return("Invalid start or end point")
        listOfRoutes = []
        Routes = self.generateRoutes(Start,End, StartTime, searched)
        for Route in Routes:
            RouteToAdd = Route_(Route)
            listOfRoutes.append(RouteToAdd)
        self.FoundRoutes = listOfRoutes
        #print(out)

    def findFlightsFrom(self, Start):
        return(self.DayInfo.getFlightsOutOf(Start))

    def findFlightsTo(self, Dest):
        return(self.DayInfo.getFlightsTo(Dest))
        
    def getDepartureAirports(self):
        return(self.DayInfo.getdepartureAirports())

    def getFoundRoutes(self):
        return(self.FoundRoutes)


class Route_Manager():
    """Route_Manager
    This class serves as a management wrapper for the Route Class. It allows for easy
    sorting and filtering of routes, making it easier to display routes to a user based on
    a variety of criteria.
    """
    def __init__(self, found_routes):
        self.routes = found_routes
        pass

    def sortST(self):
        #sorts with stops and time
        tempL = self.getRoutes()
        tempL.sort(reverse = False, key = Route_.getValue)
        return(Route_Manager(tempL))

    def getRoutes(self):
        return(self.routes)

    def sortByStops(self):
        tempL = self.getRoutes()
        tempL.sort(reverse = False, key = Route_.getNumFlights)
        return(Route_Manager(tempL))

    def filterByStops(self, n):
        out = []
        for route in self.getRoutes():
            if route.getNumFlights()-1 == n:
                out.append(route)
        return(Route_Manager(out))

    def filterLessThanNStops(self, n):
        out = []
        for route in self.getRoutes():
            if route.getNumFlights()-1 <= n:
                out.append(route)
        return(Route_Manager(out))

    def sortByTime(self):
        tempL = self.getRoutes()
        tempL.sort(reverse = False, key = Route_.getRouteTime)
        return(Route_Manager(tempL))

    def filterByTime(self):
        #Not useful
        pass