import pandas as pd
#import pyodbc

class Airport_Look_UP:
    def __init__(self, filename):
        self.file= pd.read_csv(filename)
        self.db = pd.DataFrame(self.file)
        #self.db.columns = ["id","name","city","country_name","iata_code","icao_code","latitude_deg","longitude_deg","elevation_ft","Timezone","DST", "database_time_zone", "Type", "Source"]
        #conn = pyodbc.connect('Driver={SQL Server};'
        #              'Server=RON\SQLEXPRESS;'
        #              'Database=test_database;'
        #              'Trusted_Connection=yes;')
        #cursor = conn.cursor()
        self.db.columns = ["id","ident","type","name","latitude_deg","longitude_deg","elevation_ft","continent","country_name","iso_country","region_name","iso_region","local_region","municipality","scheduled_service","gps_code","iata_code","local_code","home_link","wikipedia_link","keywords","score","last_updated"]
        
    def getLatlong(self,iata_code):
        for i in range(self.db.index.size):
            if self.db.loc[i,"iata_code"] == iata_code:
                return(self.db.loc[i,"latitude_deg"],self.db.loc[i,"longitude_deg"])
        #print("g")

    pass

aptable = Airport_Look_UP("us_airports.csv")#All_airports.csv

print(aptable.getLatlong("LHR"))
