from flask import Flask, render_template, request
from datetime import datetime


import airportData
import flightGen
import route
Airports = airportData.Airport_Look_UP("us_airports.csv")


def getPaths(Start, End,Stops):
    pathList = []
    r = flightGen.flightGen()
    r.findRoute(Start,End,datetime(2022,10,13,0,0,0),[])
    RtMnger = route.Route_Manager(r.getFoundRoutes())
    for routes in RtMnger.filterLessThanNStops(Stops).getRoutes():#filterByStops
        #print(routes)
        i = 0
        for flight in routes.getList():
            #print(Airports.getLatlong(flight.getDepartureAirport()))
            #print(Airports.getLatlong(flight.getArrivalAirport()))
            pathList.append({'lat1' : Airports.getLatlong(flight.getDepartureAirport())[0], 'long1':Airports.getLatlong(flight.getDepartureAirport())[1],
            'lat2' : Airports.getLatlong(flight.getArrivalAirport())[0], 'long2':Airports.getLatlong(flight.getArrivalAirport())[1],'steps':routes.getNumFlights(), 'flight': flight})
            i += 1
        pass
    return(pathList)
app=Flask(__name__)
@app.route('/')
@app.route('/<Start>/<End>')
@app.route('/<Start>/<End>/<Stops>')
def root(Start = "SBP", End = "MSY", Stops = 10):
    Start = Start.upper()
    End = End.upper()
    pathList = getPaths(Start, End, int(Stops))
    markers=[
        {
        'lat':0,
        'lon':0,
        'popup':'This is the middle of the map.'
        },
        {'lat':Airports.getLatlong(Start)[0],
        'lon':Airports.getLatlong(Start)[1],
        'popup':Start}
    ]
    latlongs = [{
    'lat1' : 37.6213, 'long1':-122.3790,
    'lat2' : 39.8561, 'long2':-104.6737,
    },{
    'lat1' :39.8561,'long1': -104.6737,
    'lat2' :29.9911,'long2': -90.2592}
    ]

    return render_template('index.html',markers=markers, latlongs = pathList)

if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)