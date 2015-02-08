# import urllib.request, json
# from builtins import print
#
# token = 'sDDqnqqBmkfUFSEzXoElcgzmYrtTyZGz'
# url = 'http://www.ncdc.noaa.gov/cdo-web/api/v2/data'
#
# r = urllib.request.Request(url)
# response_json = r.json()
# token = response_json[token]
#
# print(r.json)
#

import pycurl
import Weather_API.Temp_API.datasets
import Weather_API.Temp_API.data
import Weather_API.Temp_API.datacategories
import Weather_API.Temp_API.datatypes
import Weather_API.Temp_API.locationcategories
import Weather_API.Temp_API.locations
import Weather_API.Temp_API.stations

try:
    from io import BytesIO
except ImportError:
    from StringIO import StringIO as BytesIO

# Creating more user-friendly variables of each page
dataSets = Weather_API.Temp_API.datasets
dataCategories = Weather_API.Temp_API.datacategories
dataTypes = Weather_API.Temp_API.datatypes
locationCategories = Weather_API.Temp_API.locationcategories
locations = Weather_API.Temp_API.locations
stations = Weather_API.Temp_API.stations
data = Weather_API.Temp_API.data

url = "http://www.ncdc.noaa.gov/cdo-web/api/v2"


tokenParam = "sDDqnqqBmkfUFSEzXoElcgzmYrtTyZGz"

# List of Possible Requests to Add onto URL
endPoint = [
    "/datasets",             # (1) datasets
    "/datacategory",         # (2) datacategory
    "/datatypes",            # (3) datatypes
    "/locationcategories",   # (4) locationcategories
    "/locations",            # (5) locations
    "/stations",             # (6) stations
    "/data",                 # (7) data
]

# Define URL That is Desired starting with url + endPoint[n]
finalUrl = url + endPoint[0]
print(finalUrl)

# Make Request
buffer = BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, finalUrl)
c.setopt(c.WRITEDATA, buffer)
c.setopt(c.HTTPHEADER, ["token: sDDqnqqBmkfUFSEzXoElcgzmYrtTyZGz"])
c.perform()
c.close()

body = buffer.getvalue()
print(body.decode('iso-8859-1'))