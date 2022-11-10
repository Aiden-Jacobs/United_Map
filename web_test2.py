from multiprocessing.resource_sharer import stop
from flask import Flask, render_template, request
from datetime import datetime

import airportData
import flightGen
import route

Airports = airportData.Airport_Look_UP("us_airports.csv")#  All_airports.csv
r = flightGen.flightGen()

def getLinkableAP(FlightDataOb):
    """
    Returns pointList a list of dictionaries/Json of Points to be passed to the javascript
        {lat1:Float,long1:Float,lat2:Float,long2:Float,Name:Str(iata_code)}
    """
    pointList = []
    apList = FlightDataOb.getDepartureAirports()
    for a in apList:
        lat = Airports.getLatlong(a)[0]
        long = Airports.getLatlong(a)[1]
        pointList.append({'lat1' : lat, 'long1':long,
        'lat2' : lat, 'long2':long,'Name':str(a)})
    return(pointList)

def getRoutesToDisp(RtMnger):
    """
    Returns routeList a list of dictionaries of dictionaries/Json of routes to a destination to be passed to the HTML&javascript to be displayed in a list
                [{Time: Route Time in seconds, Steps: stops in Route, Flights:{flight1: str(Departure time iata_code->iata_code), flight_n: str(Departure time iata_code->iata_code)}},...] 
    
    RtMnger, is type Route_Manager
    """
    routeList = []
    i = 0 
    for routes in RtMnger.sortST().getRoutes():#filterByTime
        routeList.append({'Time':routes.getRouteTime().total_seconds(),'Steps':routes.getNumFlights()})
        routeList[i]["Flights"] = {}
        j = 0
        for flight in routes.getList():
            j += 1
            routeList[i]["Flights"]["flight"+str(j)] = str(str(flight.getDepartureTime().strftime("%H:%M:%S"))+" "+str(flight.getDepartureAirport())+"->"+str(flight.getArrivalAirport()))
        pass
        i += 1
    return(routeList)

def getFlightsToDraw(RtMnger,Stops):
    """
    Returns pathList a list of dictionaries/Json of lines/flights to be passed to the javascript
            [{lat1:Float,long1:Float,lat2:Float,long2:Float,steps:Int,flight:Str},...]

    RtMnger, is type Route_Manager
        best practice to use Route_Manager.getUniqueRoutes()
    Stops, is type Int
    """
    pathList = []
    for routes in RtMnger.filterLessThanNStops(Stops).sortByStops().getRoutes():#filterByStops
        try:# try is to filter out airports not in database
            for flight in routes.getList():
                pathList.append({'lat1' : Airports.getLatlong(flight.getDepartureAirport())[0], 'long1':Airports.getLatlong(flight.getDepartureAirport())[1],
                'lat2' : Airports.getLatlong(flight.getArrivalAirport())[0], 'long2':Airports.getLatlong(flight.getArrivalAirport())[1],'steps':routes.getNumFlights(), 'flight': flight})
            pass
        except:
            pass
    return(pathList)

def textToDateTime(time):#todo change to be datetime.now
    """Returns datetime modified for the selected filter time"""
    try:
        return(datetime(2022,10,19,int(time[0:2]),0,0))
    except:
        return(datetime(2022,10,13,0,0,0))

def getPaths(FindFlightOb,Start, End, Time, Stops = 1):#add time check 
    """
    Returns a tuple (pathList,routeList)
            pathList a list of dictionary/Json of lines/flights to be passed to the HTML&javascript
                [{lat1:Float,long1:Float,lat2:Float,long2:Float,steps:Int,flight:Str},...]
            routeList a list of dictionaries of dictionaries/Json of routes to a destination to be passed to the HTML&javascript to be displayed in a list
                [{Time: Route Time in seconds, Steps: stops in Route, Flights:{flight1: str(Departure time iata_code->iata_code), flight_n: str(Departure time iata_code->iata_code)}},...] 
    
    FindFlightOb, is type Route_Finder for day of interest 
    Start, is type Str of an iata_code
    End, is type Str of an iata_code
    Time, is type datetime 
            used to get routes after it
    Stops, is type Int
    """
    pathList = []
    routeList = []
    Start = Start.upper()
    End = End.upper()
    if Start != '' and End != '':
        if FindFlightOb.checkValidStartEnd(Start, End):
            FindFlightOb.findRoute(Start,End,datetime(2022,10,13,0,0,0),[], int(Stops))
    elif Start != '' and End == '' and FindFlightOb.checkValidAirport(Start):
        FindFlightOb.findFlightsFrom(Start)
    elif Start == '' and End != '' and FindFlightOb.checkValidAirport(End):
        FindFlightOb.findFlightsTo(End)
    else:
        return([],[])
    RtMnger = route.Route_Manager(FindFlightOb.getFoundRoutes())
    RtMnger = RtMnger.filterByStartTime(Time)
    pathList = getFlightsToDraw(RtMnger.getUniqueRoutes(), Stops)
    routeList = getRoutesToDisp(RtMnger)
    if Start == '' and End == '':
        return([],[])
    else:
        return(pathList,routeList)


app=Flask(__name__)

#@app.route('/<Start>/<End>')
#@app.route('/<Start>/<End>/<Stops>')
@app.route('/<Start>/<End>/<Stops>',methods = ['POST', 'GET'])
@app.route('/',methods = ['POST', 'GET'])
def root(Start = "", End = "", Stops = 1, filterTime = datetime(2022,10,13,0,0,0)): #todo switch to time.now 
    Start = Start.upper()
    End = End.upper()
    pathList = []
    pointList = []
    pointList = getLinkableAP(r)
    routes = []
    markers = []
    RandP = []
    if request.method == 'POST':
        form_data = request.form
        print(form_data)
        if form_data['FromReq'] != '' and form_data['ToReq'] != '':
            Start = form_data['FromReq'].upper()
            End = form_data['ToReq'].upper()
            if form_data['NumStopsReq'] != '':
                Stops = form_data['NumStopsReq']
                #if type(Stops) !=  int:  todo check if works
                #    Stops = 0
            latlong1 = Airports.getLatlong(Start)
            latlong2 = Airports.getLatlong(End)
            if latlong1 != None and latlong2 != None:
                markers.append({'lat':latlong1[0],
                                'lon':latlong1[1],
                                'popup':"Start "+Start})
                markers.append({'lat':latlong2[0],
                                'lon':latlong2[1],
                                'popup':"End "+End})
        if form_data['FromReq'] != '' and form_data['ToReq'] == '':
            Start = form_data['FromReq'].upper()
            latlong1 = Airports.getLatlong(Start)
            if latlong1 != None:
                markers.append({'lat':latlong1[0],
                                'lon':latlong1[1],
                                'popup':"Start "+Start})
        if form_data['FromReq'] == '' and form_data['ToReq'] != '':
            End = form_data['ToReq'].upper()
            latlong2 = Airports.getLatlong(End)
            if r.checkValidAirport(Start):
                markers.append({'lat':latlong2[0],
                                'lon':latlong2[1],
                                'popup':"End "+End})
        if form_data['TimeList'] != '':
            filterTime = textToDateTime(form_data['TimeList'])
        print(filterTime)
        RandP =  getPaths(r,Start, End,filterTime, int(Stops))
        pathList = RandP[0]
        routes = RandP[1]

#        markers=[
#            {'lat':Airports.getLatlong(Start)[0],
#            'lon':Airports.getLatlong(Start)[1],
#            'popup':"Start "+Start},
#            {'lat':Airports.getLatlong(End)[0],
#            'lon':Airports.getLatlong(End)[1],
#            'popup':"End "+End}
#            ]
    
    return render_template('index.html',markers=markers, latlongs = pathList, pointList = pointList, r = routes)




if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)