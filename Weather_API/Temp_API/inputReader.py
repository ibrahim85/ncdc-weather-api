__author__ = 'Thor'

import Weather_API.Temp_API.datasets
import Weather_API.Temp_API.data
import Weather_API.Temp_API.datacategories
import Weather_API.Temp_API.datatypes
import Weather_API.Temp_API.locationcategories
import Weather_API.Temp_API.locations
import Weather_API.Temp_API.stations

dataSets = Weather_API.Temp_API.datasets
dataCategories = Weather_API.Temp_API.datacategories
dataTypes = Weather_API.Temp_API.datatypes
locationCategories = Weather_API.Temp_API.locationcategories
locations = Weather_API.Temp_API.locations
stations = Weather_API.Temp_API.stations
data = Weather_API.Temp_API.data

# List of Possible Requests to Add onto URL
endPointList = [
    "/datasets",             # (0) datasets
    "/datacategory",         # (1) datacategory
    "/datatypes",            # (2) datatypes
    "/locationcategories",   # (3) locationcategories
    "/locations",            # (4) locations
    "/stations",             # (5) stations
    "/data",                 # (6) data
]

endPoint = input("Type Desired Endpoint :" '\n'
                 "Data Sets" '\n'
                 "Data Category" '\n'
                 "Data Types" '\n'
                 "Locational Categories" '\n'
                 "Locations" '\n'
                 "Stations" '\n'
                 "Data")

# Taking Input From User To Determine
if endPoint.__contains__("data sets"):
    parameterString = dataSets.parameter
    urlAdd = endPointList[0] + parameterString
elif endPoint.__contains__("data category"):
    urlAdd = endPointList[1]
elif endPoint.__contains__("data types"):
    urlAdd = endPointList[2]
elif endPoint.__contains__("location categories"):
    urlAdd = endPointList[3]
elif endPoint.__contains__("locations"):
    urlAdd = endPointList[4]
elif endPoint.__contains__("stations"):
    urlAdd = endPointList[5]
elif endPoint.__contains__("data"):
    urlAdd = endPointList[6]
