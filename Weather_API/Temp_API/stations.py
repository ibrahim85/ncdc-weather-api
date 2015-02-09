__author__ = 'Thor'

dataTypeParam = [
    "?datasetid",           # (0)   GHCNDMS
    "?locationid",          # (1)   FIPS:37
    "?datacategoryid"       # (3)   TEMP
    "?datatypeid",          # (3)   ACMH
    "?extent",              # (4)   47.5204
    "?startdate",           # (5)   1970-10-03
    "?enddate",             # (6)   2012-09-10
    "?sortfield",           # (7)   name
    "?sortorder",           # (8)   desc
    "?limit",               # (9)   42
    "?offset",              # (10)  24
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
                           "   Data Category ID," '\n'
                           "   Data Type ID," '\n'
                           "   Start Date," '\n'
                           "   End Date," '\n'
                           "   Sort Field," '\n'
                           "   Sort Order," '\n'
                           "   Limit," '\n'
                           "   Offset")
            param1.lower()

            if param1.__contains__("data set"):
                dataSpec = "=" + input("Enter ID (Example - GHCNDMS):")
                parameter = dataTypeParam[0] + dataSpec
                params = input("Would you like to add another?")

            elif param1.__contains__("location category"):
                dataSpec = "=" + input("Enter ID (Example - FIPS:37):")
                parameter = dataTypeParam[1] + dataSpec
                params = input("Would you like to add another?")

            elif param1.__contains__("data category"):
                dataSpec = "=" + input("Enter ID (Example - TEMP):")
                parameter = dataTypeParam[2] + dataSpec
                params = input("Would you like to add another?")

            elif param1.__contains__("data type"):
                dataSpec = "=" + input("Enter ID (Example - ACMH):")
                parameter = dataTypeParam[3] + dataSpec
                params = input("Would you like to add another?")

            elif param1.__contains__("extent"):
                dataSpec = "=" + input("Enter ID (Example - 47.5204, -122.2047):")
                parameter = dataTypeParam[4] + dataSpec
                params = input("Would you like to add another?")

            elif param1.__contains__("start date"):
                dataSpec = "=" + input("Enter ID (Example - 1970-10-03):")
                parameter = dataTypeParam[5] + dataSpec
                params = input("Would you like to add another?")

            elif param1.__contains__("end date"):
                dataSpec = "=" + input("Enter ID (Example - 2012-09-10):")
                parameter = dataTypeParam[6] + dataSpec
                params = input("Would you like to add another?")

            elif param1.__contains__("sort field"):
                dataSpec = "=" + input("Enter ID (Example - name):")
                parameter = dataTypeParam[7] + dataSpec
                params = input("Would you like to add another?")

            elif param1.__contains__("sort order"):
                dataSpec = "=" + input("Enter ID (Example - desc):")
                parameter = dataTypeParam[8] + dataSpec
                params = input("Would you like to add another?")

            elif param1.__contains__("limit"):
                dataSpec = "=" + input("Enter ID (Example - 42):")
                parameter = dataTypeParam[9] + dataSpec
                params = input("Would you like to add another?")

            elif param1.__contains__("offset"):
                dataSpec = "=" + input("Enter ID (Example - 24):")
                parameter = dataTypeParam[10] + dataSpec
                params = input("Would you like to add another?")

            else:
                break

            if params.__contains__("y"):
                dataSpec = "&"

    return parameter