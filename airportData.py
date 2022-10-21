import pandas as pd

class Airport_Look_UP:
    def __init__(self, filename):
        self.file= pd.read_csv(filename)
        self.file.columns = ["id","name","city","country_name","iata_code","icao_code","latitude_deg","longitude_deg","elevation_ft","Timezone","DST", "database_time_zone", "Type", "Source"]
        #self.file.columns = ["id","ident","type","name","latitude_deg","longitude_deg","elevation_ft","continent","country_name","iso_country","region_name","iso_region","local_region","municipality","scheduled_service","gps_code","iata_code","local_code","home_link","wikipedia_link","keywords","score","last_updated"]
        
    def getLatlong(self,iata_code):
        for i in range(self.file.index.size):
            if self.file.loc[i,"iata_code"] == iata_code:
                return(self.file.loc[i,"latitude_deg"],self.file.loc[i,"longitude_deg"])

    pass

aptable = Airport_Look_UP("All_airports.csv")

aptable.getLatlong("ASE")
