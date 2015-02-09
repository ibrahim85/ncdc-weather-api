from Weather_API.Temp_API import data, \
    datacategories, datasets, datatypes, \
    locationcategories, locations, stations
__author__ = 'Thor'


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
def main():
    endPoint = input("Type Desired Endpoint :" '\n'
                     "   Data Sets" '\n'
                     "   Data Category" '\n'
                     "   Data Types" '\n'
                     "   Locational Categories" '\n'
                     "   Locations" '\n'
                     "   Stations" '\n'
                     "   Data")

    # Taking Input From User To Determine
    if endPoint.__contains__("data sets"):
        parameterString = datasets.main()
        append = endPointList[0]
    elif endPoint.__contains__("data category"):
        parameterString = datacategories.main()
        append = endPointList[1]
    elif endPoint.__contains__("data types"):
        parameterString = datatypes.main()
        append = endPointList[2]
    elif endPoint.__contains__("location categories"):
        parameterString = locationcategories.main()
        append = endPointList[3]
    elif endPoint.__contains__("locations"):
        parameterString = locations.main()
        append = endPointList[4]
    elif endPoint.__contains__("stations"):
        parameterString = stations.main()
        append = endPointList[5]
    elif endPoint.__contains__("data"):
        parameterString = data.main()
        append = endPointList[6]

    urlAdd = (append + parameterString)

    return urlAdd