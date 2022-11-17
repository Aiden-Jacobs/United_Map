from multiprocessing.resource_sharer import stop
from flask import Flask, render_template, request
from datetime import datetime

import airportData
import flightGen
import webElements

Airports = airportData.Airport_Look_UP("us_airports.csv")#  All_airports.csvnikonos vFujifilm
r = flightGen.flightGen()

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
    pointList = webElements.getLinkableAP(Airports,r)
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
            filterTime = webElements.textToDateTime(form_data['TimeList'])
        print(filterTime)
        RandP =  webElements.getPaths(Airports,r,Start, End,filterTime, int(Stops))
        pathList = RandP[0]
        routes = RandP[1]

    #    markers=[
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