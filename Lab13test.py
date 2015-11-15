from lab13airport import *
import csv

atlas = AirportAtlas()
print(atlas.getAirport("DUB"))

while True:
    try:
        userCode1= (str(input("enter 3 letter airport code:").upper()))


    userCode2= (str(input("enter 3 letter airport code:").upper()))

    if userCode1 not in atlas.airportDic or userCode2 not in atlas.airportDic:
        print ("Try again")
    else:
        break



    # try:
    #     if userCode1 in AirportAtlas.airportDic and userCode2 in AirportAtlas.airportDic
    # except (TypeError, ValueError, OverflowError) as errorMessage:
    #     print (errorMessage)
    # else:
    #     print("Distance between ", userCode1, "and ", userCode2, " = ", distance, "km")
    #     break


    # try:
    #     distance = atlas.getDistanceBetweenAirports(userCode1, userCode2)
    # except (TypeError, ValueError, OverflowError) as errorMessage:
    #     print (errorMessage)
    # else:
    #     print("Distance between ", userCode1, "and ", userCode2, " = ", distance, "km")
    #     break


#
# distance = atlas.getDistanceBetweenAirports("DUB", "JFK")
# print("Distance between DUB and JFK is = ", distance, "km")



#atlas.loadData(AirportAtlas)
#AirportAtlas.loadData("airports.csv")
#AirportAtlas.airportdic



