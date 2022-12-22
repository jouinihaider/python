from flight import Flight
from airport import Airport


class FlightPath:

    start= ''
    airport = ''
    end= ''
    chemins= []

    def __init__(self,src_airport : Airport):

        self.start = True
        self.airport = src_airport.code
        self.end = False
        self.chemins.append(self)

    def add(self,dst_airport : Airport, via_flight : Flight):
        pass
    
    def flights(self): 
        pass 

    def airports(self): 
        pass 

    def steps(self): 
        pass 

    def duration(self): 
        pass 


