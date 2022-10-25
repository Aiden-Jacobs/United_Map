from flask import Flask, render_template, request
from datetime import datetime


import airportData
import flightGen
import route
Airports = airportData.Airport_Look_UP("us_airports.csv")#  All_airports.csv
r = flightGen.flightGen()

def getDepartureAP(FlightDataOb):
    pointList = []
    apList = FlightDataOb.getDepartureAirports()
    for a in apList:
        lat = Airports.getLatlong(a)[0]
        long = Airports.getLatlong(a)[1]
        pointList.append({'lat1' : lat, 'long1':long,
        'lat2' : lat, 'long2':long,'Name':str(a)})
    return(pointList)

def getConnectionsPath(FlightDataOb,start,pl):
    out = []
    f = FlightDataOb.findFlightsFrom(start.upper())
    for dest in f:
        try:
            lat = Airports.getLatlong(start.upper())[0]
            long = Airports.getLatlong(start.upper())[1]
            pl.append({'lat1' : lat, 'long1':long,
            'lat2' : lat, 'long2':long,'Name':str(start.upper())})
            out.append({'lat1' : lat, 'long1':long,
                'lat2' : Airports.getLatlong(dest.getArrivalAirport())[0], 'long2':Airports.getLatlong(dest.getArrivalAirport())[1],'steps':2, 'flight': 1})
        except:
            pass
    print("-----",f)
    return(out)
    pass

def valueGetTime(item):
    ti = item.get('Time')
    return(ti)

def getPaths(FlightDataOb,Start, End,Stops):#add time check
    pathList = []
    routeList = []
    if FlightDataOb.checkValidStartEnd(Start, End):
        FlightDataOb.findRoute(Start,End,datetime(2022,10,13,0,0,0),[])
        RtMnger = route.Route_Manager(r.getFoundRoutes())
        i = 0
        for routes in RtMnger.filterLessThanNStops(Stops).sortByStops().getRoutes():#filterByStops
            #print(routes.getRouteTime())
            routeList.append({'Time':routes.getRouteTime().total_seconds(),'Steps':routes.getNumFlights()})
            routeList[i]["Flights"] = {}
            j = 0
            for flight in routes.getList():
                j += 1
                routeList[i]["Flights"]["flight"+str(j)] = str(str(flight.getDepartureTime().strftime("%H:%M:%S"))+" "+str(flight.getDepartureAirport())+"->"+str(flight.getArrivalAirport()))
                #print(Airports.getLatlong(flight.getDepartureAirport()))
                #print(Airports.getLatlong(flight.getArrivalAirport()))
                pathList.append({'lat1' : Airports.getLatlong(flight.getDepartureAirport())[0], 'long1':Airports.getLatlong(flight.getDepartureAirport())[1],
                'lat2' : Airports.getLatlong(flight.getArrivalAirport())[0], 'long2':Airports.getLatlong(flight.getArrivalAirport())[1],'steps':routes.getNumFlights(), 'flight': flight})
            pass
            i += 1
    #new_list = dict(sorted(routeList.items(), key=lambda item: item[1]))
    #print(routeList)
    return(pathList,routeList)

def orderRoutes(routeList):

    pass

app=Flask(__name__)
@app.route('/')
#@app.route('/<Start>/<End>')
#@app.route('/<Start>/<End>/<Stops>')
@app.route('/<Start>/<End>/<Stops>',methods = ['POST', 'GET'])
def root(Start = "SBP", End = "MSY", Stops = 2):
    Start = Start.upper()
    End = End.upper()
    pathList = []
    pointList = []
    if request.method == 'POST':
        form_data = request.form
        print(form_data)
        if form_data['FromReq'] != '' and form_data['ToReq'] != '':
            Start = form_data['FromReq'].upper()
            End = form_data['ToReq'].upper()
            if form_data['NumStopsReq'] != '':
                Stops = form_data['NumStopsReq']

        pointList = getDepartureAP(r)
        RandP =  getPaths(r,Start, End, int(Stops))
        pathList = RandP[0]
        routes = RandP[1]
        if form_data['FromReq'] != '' and form_data['ToReq'] == '':
            pathList = getConnectionsPath(r, form_data['FromReq'],pointList)

    markers=[
        {'lat':Airports.getLatlong(Start)[0],
        'lon':Airports.getLatlong(Start)[1],
        'popup':"Start "+Start},
        {'lat':Airports.getLatlong(End)[0],
        'lon':Airports.getLatlong(End)[1],
        'popup':"End "+End}
        ]
    latlongs = [{
    'lat1' : 37.6213, 'long1':-122.3790,
    'lat2' : 37.6213, 'long2':-122.3790,'steps':2, 'flight': 4
    },{
    'lat1' :39.8561,'long1': -104.6737,
    'lat2' :29.9911,'long2': -90.2592,'steps':1, 'flight': 4}
    ]
    
    return render_template('index.html',markers=markers, latlongs = pathList, pointList = pointList, r = routes)


if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)