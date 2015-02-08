__author__ = 'Thor'


#   URL: http://www.ncdc.noaa.gov/cdo-web/api/v2/data
#   APPENDS: dataTypeParam[n]ARGS
#
#   dataTypeParam[0] required - Data Set ID
#   dataTypeParam[4] required - Start Date
#   dataTyoeParam[5] required - End Date

dataTypeParam = [
    "?datasetid=",       # (0)   GHCNDMS        **
    "?datatypeid=",      # (1)   ACMH
    "?locationid=",      # (2)   FIPS:37
    "?stationdid=",      # (3)   COOP:010957
    "?startdate=",       # (4)   1970-10-03     **
    "?enddate=",         # (5)   2012-09-10     **
    "?sortfield=",       # (6)   name
    "?sortorder=",       # (7)   desc
    "?limit=",           # (8)   42
    "?offset=",          # (9)   24
    "?includemetadata="  # (10)  false
]

Args = [
    # # Enter in Data Sets
]