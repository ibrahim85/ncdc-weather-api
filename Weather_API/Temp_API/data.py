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

def main():
    parameter = ""
    params = input("Would you like to add any parameters?")

    while params[0] == "y":
        if params == "yes":
            param1 = input("Which parameter?" '\n'
                           "   Data Set ID (Required)," '\n'
                           "   Data Type ID," '\n'
                           "   Location," '\n'
                           "   Station ID," '\n'
                           "   Start Date (Required)," '\n'
                           "   End Date (Required)," '\n'
                           "   Sort Field," '\n'
                           "   Sort Order," '\n'
                           "   Limit," '\n'
                           "   Offset," '\n'
                           "   Include Meta Data")
            param1.lower()

            if param1.__contains__("data set"):
                dataSpec = "=" + input("Enter ID (Example - GHCNDMS):")
                parameter = dataTypeParam[0] + dataSpec
                params = input("Would you like to add another?")

            elif param1.__contains__("data type"):
                dataSpec = "=" + input("Enter ID (Example - ACMH):")
                parameter = dataTypeParam[1] + dataSpec
                params = input("Would you like to add another?")

            elif param1.__contains__("location"):
                dataSpec = "=" + input("Enter ID (Example - FIPS:37):")
                parameter = dataTypeParam[2] + dataSpec
                params = input("Would you like to add another?")

            elif param1.__contains__("station"):
                dataSpec = "=" + input("Enter ID (Example - COOP:010957):")
                parameter = dataTypeParam[3] + dataSpec
                params = input("Would you like to add another?")

            elif param1.__contains__("start date"):
                dataSpec = "=" + input("Enter ID (Example - 1970-10-03):")
                parameter = dataTypeParam[4] + dataSpec
                params = input("Would you like to add another?")

            elif param1.__contains__("end date"):
                dataSpec = "=" + input("Enter ID (Example - 2012-09-10):")
                parameter = dataTypeParam[5] + dataSpec
                params = input("Would you like to add another?")

            elif param1.__contains__("sort field"):
                dataSpec = "=" + input("Enter ID (Example - name):")
                parameter = dataTypeParam[6] + dataSpec
                params = input("Would you like to add another?")

            elif param1.__contains__("sort order"):
                dataSpec = "=" + input("Enter ID (Example - desc):")
                parameter = dataTypeParam[7] + dataSpec
                params = input("Would you like to add another?")

            elif param1.__contains__("limit"):
                dataSpec = "=" + input("Enter ID (Example - 42):")
                parameter = dataTypeParam[8] + dataSpec
                params = input("Would you like to add another?")

            elif param1.__contains__("offset"):
                dataSpec = "=" + input("Enter ID (Example - 24):")
                parameter = dataTypeParam[9] + dataSpec
                params = input("Would you like to add another?")

            elif param1.__contains__("include meta"):
                dataSpec = "=" + input("Enter ID (Example - false):")
                parameter = dataTypeParam[10] + dataSpec
                params = input("Would you like to add another?")

            else:
                break

            if params.__contains__("y"):
                dataSpec = "&"

    return parameter