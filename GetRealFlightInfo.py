import bs4, requests
import datetime

Airport = "kef"
flight_List = []

getPage = requests.get('https://united-airlines.flight-status.info/'+str(Airport)+'-departures')
getPage.raise_for_status()
pageCode = bs4.BeautifulSoup(getPage.text, 'html.parser')
tbody = pageCode.select("table")
tr = tbody[0].select("tr")
#print(tr)
for ti in tr:
    td = ti.select("td")
    Flight_Number = ""
    departure_time =""
    AP_code =""
    FlightTimeHours = ""
    FlightTimeMins = ""
    for i in range(len(td)):
        if i == 0:
            #print(td[i].text[17:23])#Flight Number
            Flight_Number=td[i].text[17:23]
            Flight_Number.strip()
            #print()
        if i == 1:
            departure_time = td[i].text#time hh:mm
            departure_time.strip()
        if i == 2:
            #print(td[i].text[1:4])#airport code
            AP_code = td[i].text[1:4]
            #print(len(td[i].text))
        #print(td[i])
        #print(len(td[i]))
    if Flight_Number != "":
        if ord(Flight_Number[5]) == 10:
            getPage2 = requests.get('https://united-airlines.flight-status.info/ua-'+str(Flight_Number[2:5]))
            Flight_Number=Flight_Number[0:5]
        else:
            getPage2 = requests.get('https://united-airlines.flight-status.info/'+str(Flight_Number))
        #getPage2.raise_for_status()
        pageCode2 = bs4.BeautifulSoup(getPage2.text, 'html.parser')
        gfg = pageCode2.find("span", string="Flight Duration: ")
        if gfg != None:
            #print(gfg.next.next)
            #print("A hours ",gfg.next.next[0])#hours
            #print("A min ",gfg.next.next[10:12])#min
            FlightTimeHours = gfg.next.next[0:2]
            FlightTimeHours.strip()
            FlightTimeMins = gfg.next.next[10:13]
            print(Flight_Number,departure_time,Airport.upper(),AP_code,FlightTimeHours,FlightTimeMins)
            flight_List.append([Flight_Number,departure_time,Airport.upper(),AP_code,FlightTimeHours,FlightTimeMins])
print(len(tr))
print("----------")
print(flight_List)