import os
import csv
from math import sin,cos,acos,pi
radius_earth = 6371

class Airport:
    def __init__(self, airportID, airportName, cityName,country, code, icaoCode,latitude, longitude, altitude, timeOffset, dst, tz):

        self.airportID = airportID #0
        self.airportName = airportName #1
        self.cityName = cityName #2
        self.country = country #3
        self.code = code #4
        self.icaoCode = icaoCode #5
        self.latitude = latitude #6 float
        self.longitude = longitude #7 float
        self.altitude = altitude #8
        self.timeOffset = timeOffset #9
        self.dst = dst #10
        self.tz = tz #11

    def __str__(self):
        return " {} (Name: {} {} {} lat: {} long: {})".format\
            (self.code, self.airportName, self.cityName, self. country, self.latitude,self.longitude)

class AirportAtlas:
    airport_fn = "airport.csv"                                      #assigning CSV file in directory to variable

    def __init__(self, airport_file = airport_fn):                  #default paramater ='airportfn' (assigned above), unless told otherwise
        self.airportDic = self.buildAirportDic(airport_file)        # assigning the return of method as the dictionary

    def buildAirportDic (self, filename):                           #reads a file, and populates dictionary
        airportDic={}
        try:
            with open(os.path.join(filename),"rt", encoding = "utf8") as f:
                reader = csv.reader(f)
                for line in reader:
                    try:                                                #key:value, where value is object 'Airport'
                        airportDic[line[4]] = Airport (line[0],line[1],line[2],line[3],line[4],line[5],\
                                                       float(line[6]),float(line[7]),line[8],line[9],line[10],line[11])
                        #print(airportDic[line[1]])
                    except KeyError:
                        continue                                        #continues with loop if airport code KEY not found

        except (IOError, FileNotFoundError) as errorMessage:   #IOError: #FileNotFoundError
            print (errorMessage)
        #else:
            # for line in reader:
            #     try:                                                #key:value, where value is object 'Airport'
            #         airportDic[line[4]] = Airport (line[0],line[1],line[2],line[3],line[4],line[5],\
            #                                        float(line[6]),float(line[7]),line[8],line[9],line[10],line[11])
            #         #print(airportDic[line[1]])
            #     except KeyError:
            #         continue                                        #continues with loop if airport code KEY not found
        return airportDic

    def getAirport(self, code):                                     #takes code as KEY and returns details of Airport object
        try:
            return self.airportDic[code.upper()]
        except KeyError:
            return None

    def getDistanceBetweenAirports(self, code1, code2):             #uses static methods to calculate distance between 2 airports
        try:
            airport1 = self.getAirport(code1) #creating "airport1" object using 'code1' key (this returns the 'value' which is an object
            airport2 = self.getAirport(code2)
        except KeyError:
            print ("the first one")
            return None
            # lat1 = self.getAirport(code1)
            # long1 = self.getAirport(code1)
        #while True:
        try:
            lat1 = airport1.latitude                                    #pulls the latitude attribute from the Airport object.
            long1 = airport1.longitude
            lat2 = airport2.latitude
            long2 = airport2.longitude
        except AttributeError as errorMessage:
            print ("Invalid input, try again" , errorMessage)
            return None
        else:
            distance = AirportAtlas.calcDistance(lat1,lat2,long1,long2) #calling static method
                #break

        return distance

    @staticmethod
    def calcDistance(lat1,lat2, long1, long2):                      #takes lats&longs converts to radials, returns distance.
        theta1, theta2, phi1, phi2 = AirportAtlas.definetheta(lat1, lat2, long1, long2)

        distance = (acos(sin(theta1)*sin(theta2)*cos(phi1-phi2)+(cos(theta1)*cos(theta2)))*radius_earth)
        return distance


    @staticmethod
    def definetheta(lat1,lat2, long1, long2):               #converts degrees to radians
        theta1 = 90 - lat1              #90 - , as there are 2 pole points on earth, we need to know where our point is in relation to the equator/poles
        theta1 = theta1*((2*pi)/360)

        theta2 = 90 - lat2
        theta2 = theta2 * ((2*pi)/360)

        ###convert longitude radiants without 90-, as the equator doesn't have points/poles.
        phi1 = long1 * ((2*pi)/360)
        phi2 = long2 * ((2*pi)/360)

        return theta1, theta2, phi1, phi2  ## "releases" thetas and phis, by returning them after the lats and longs have been converted. Then used in function below.



def main():
    myAtlas = AirportAtlas()

if __name__ == "__main__":
    main()