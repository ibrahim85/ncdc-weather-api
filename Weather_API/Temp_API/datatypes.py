__author__ = 'Thor'

dataTypeParam = [
    "?datasetid",           # (0)   ACMH
    "?locationid",          # (1)   FIPS:37
    "?stationdid",          # (2)   COOP:010957
    "?datacategoryid"       # (3)   TEMP
    "?startdate",           # (4)   1970-10-03
    "?enddate",             # (5)   2012-09-10
    "?sortfield",           # (6)   name
    "?sortorder",           # (7)   desc
    "?limit",               # (8)   42
    "?offset",              # (9)   24
]

def main():
    parameter = ""
    dataSpec = "="
    params = input("Would you like to add any parameters?")

    while params[0] == "y":
        if params == "yes":
            param1 = input("Which parameter?" '\n'
                           "   Data Set ID," '\n'
                           "   Location ID," '\n'
                           "   Station ID," '\n'
                           "   Data Category ID," '\n'
                           "   Start Date," '\n'
                           "   End Date," '\n'
                           "   Sort Field," '\n'
                           "   Sort Order," '\n'
                           "   Limit," '\n'
                           "   Offset")
            param1.lower()

            if param1.__contains__("data set id"):
                dataSpec = "=" + input("Enter ID (Example - GHCNDMS):")
                parameter = dataTypeParam[0] + dataSpec
                params = input("Would you like to add another?")

            elif param1.__contains__("location id"):
                dataSpec = "=" + input("Enter ID (Example - FIPS:37):")
                parameter = dataTypeParam[1] + dataSpec
                params = input("Would you like to add another?")

            elif param1.__contains__("station id"):
                dataSpec = "=" + input("Enter ID (Example - COOP:010957):")
                parameter = dataTypeParam[2] + dataSpec
                params = input("Would you like to add another?")

            elif param1.__contains__("data category id"):
                dataSpec = "=" + input("Enter ID (Example - TEMP):")
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

            else:
                break

            if params.__contains__("y"):
                dataSpec = "&"

    return parameter