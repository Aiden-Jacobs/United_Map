import random
from datetime import datetime, timedelta
from sys import argv
# | my classes
# v 
import flight
import dayinfo
import route
seed = 2346 #234
random.seed(seed)
print(argv[0])
print("Seed", seed)

##setup flight data
def flightGen():
    Airports = {"SFO":["IAH", "MSP", "ORD", "DEN","MSY","SBP"],
    "SBP":["SFO","DEN","LAX"],
    "LAX":["SFO","SBP","DEN","ASE","IAH","ORD"],
    "MSP":["SFO","DEN","IAH","ORD"],
    "DEN":["IAH","MSP","MSY","SBP","SFO","LAX","ASE","ORD"],
    "ORD":["IAH","MSP","MSY","DEN","SFO","LAX"],
    "ASE":["DEN","LAX"],#IAH
    "IAH":["MSP","MSY","SFO","LAX","ORD","DEN"],#ASE
    "MSY":["IAH","SFO","ORD", "DEN"]}

    FtimesAP =[["DEN","SBP",[2,40,0]]
    ,["SBP","DEN",[2,40,0]]
    ,["MSY","DEN",[2,40,0]]
    ,["DEN","MSY",[2,40,0]]
    ,["SFO","SBP",[1,3,0]]
    ,["SBP","SFO",[1,3,0]]
    ,["MSY","SFO",[4,15,0]]
    ,["SFO","MSY",[4,15,0]]
    ,["IAH","DEN",[2,29,0]]
    ,["DEN","IAH",[2,29,0]]
    ,["MSY","IAH",[1,16,0]]
    ,["IAH","MSY",[1,16,0]]
    ,["LAX","SBP",[1,11,0]]
    ,["SBP","LAX",[1,11,0]]
    ,["IAH","LAX",[3,29,0]]
    ,["LAX","IAH",[3,29,0]]
    ,["DEN","LAX",[2,22,0]]
    ,["LAX","DEN",[2,22,0]]
    ,["IAH","SFO",[3,57,0]]
    ,["SFO","IAH",[3,57,0]]
    ,["ASE","DEN",[0,56,0]]
    ,["DEN","ASE",[0,56,0]]
    ,["ASE","LAX",[2,16,0]]
    ,["LAX","ASE",[2,16,0]]]

    FlightsFromAP9 = {"SFO":[],
                    "SBP":[],
                    "LAX":[],
                    "MSP":[],
                    "DEN":[],
                    "ORD":[],
                    "ASE":[],
                    "IAH":[],
                    "MSY":[]}

    #setup flight data
    #used in setup only
    def findTimeInAir(listOfF, st,end):
        for f in listOfF:
            if f.getDepartureAirport() == st and f.getArrivalAirport() == end:

                return(f.GetFlightTime().seconds)
        return(0)


    #setup flight data
    Day1 = dayinfo.INFO_for_Day()
    print(random.randint(1,4))
    for Ap in Airports:
        #can add in code to load airports in from airports
        for dest in Airports[Ap]:
            FPD = random.randint(1,10)#(1,5)
            for i in range(FPD):
                dptTime = datetime(2022,10,13,random.randint(5,22),random.randint(0,59),0)
                
                ft = 0
                if Day1.containsApInDp(Ap):
                    ft = findTimeInAir(Day1.FlightsFromAP[Ap],Ap,dest)
                if ft == 0:
                    for times in FtimesAP:
                        if times[0] == Ap and times[1] == dest:
                            ft = times[2][0]*60*60+(times[2][1]*60)+times[2][2]
                        else:
                            ft = random.randint(40*60,60*60*5)
                
                Day1.addFlight((flight.Flight_(Ap, dest, dptTime,ft)))
            #print(Ap,FPD,"flights per day to", dest)
        #print(Ap, "flights per day", FPD, Airports[Ap])
    ## end setup flight data


    ## main for after data gen
    print(datetime(2022,10,13,0,0,0))
    #print(Day1.FlightsFromAP)
    findOB = route.Route_Finder(Day1)
    return(findOB)
    findOB.findRoute("SBP","MSY",datetime(2022,10,13,10,0,0),[])
    RtMnger = route.Route_Manager(findOB.getFoundRoutes())
    print("------------")

    for r in RtMnger.sortST().getRoutes():
        print()
        print(str(r))

    #print(findOB.findFlightsFrom("SBP"))

    print("\n---Done---")