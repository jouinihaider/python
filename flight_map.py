
import csv
from flight import Flight
from airport import Airport


class FlightMap:
    
    listAreport =  [Airport]
    listFlights =  [Flight]

    def import_airports(self,csv_file):
        with open(csv_file) as csvfile:
            list = csv.reader(csvfile, delimiter=' ', quotechar='"')

            for row in list:
                obj = Airport()
                obj.name = row[0]
                obj.code = row[1].replace(',', '')
                obj.lat = row[2]
                obj.long = row[3]
                self.listAreport.append(obj)

    def import_flights(self,csv_file):
        with open(csv_file) as csvfile:
            list = csv.reader(csvfile, delimiter=' ', quotechar='"')
            for row in list:
                obj = Flight()
                obj.src_code = row[0].replace(',', '')
                obj.dst_code = row[1].replace(',', '')
                obj.duration = row[2]
                self.listFlights.append(obj)
    
    def airports(self):
        return self.listAreport
    
    def flights(self):
        return self.listFlights

    def airport_find(self,airport_code):
        for air in self.listAreport:
            print(str(air.code) , str(airport_code))
            if(str(air.code) == str(airport_code)):
                return air
        return None
    
    def flight_exist(self,src_airport_code, dst_airport_code): 
        for item in self.listFlights:
            print(item.src_code,'=',src_airport_code)
            if((item.src_code == src_airport_code) and (item.dst_code == dst_airport_code)):
                return True
        return False
    
    def flights_where(self,airport_code): 
        list_vol = []
        for item in self.listFlights:
            if((item.src_code == airport_code) or (item.dst_code == airport_code)):
                list_vol.append(item)
        return list_vol
    
    def airports_from(self,airport_code): 
        list_flight = self.flights_where(airport_code)
        list_vol = []
        for item in list_flight:
            if(item.src_code == airport_code):
                list_vol.append(self.airport_find(item.dst_code))
        return list_vol





