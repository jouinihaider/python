# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.


from flight import Flight
from airport import Airport
from flight_map import FlightMap
from flight_path import FlightPath


pathAreport  = '/Users/xelerolab/Desktop/ESTIAM/Python/files/aeroports.csv'    
pathFlights  = '/Users/xelerolab/Desktop/ESTIAM/Python/files/flights.csv'


FlightMapT = FlightMap()
FlightPathT = FlightPath(Airport())


# print("listAreport = ",FlightMapT.listAreport)
# print("import_airports = ",FlightMapT.import_airports(pathAreport))
# print("import_airports = ",FlightMapT.import_flights(pathFlights))
# print("airport_find = ",FlightMapT.airports_from('AKL'))
print("Flight Path = ",FlightPathT)

        
