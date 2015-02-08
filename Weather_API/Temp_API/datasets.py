__author__ = 'Thor'

dataTypeParam = [
    "?datatypeid",           # (0)   ACMH
    "?locationid",           # (1)   FIPS:37
    "?stationdid",           # (2)   COOP:010957
    "?startdate",            # (3)   1970-10-03
    "?enddate",              # (4)   2012-09-10
    "?sortfield",            # (5)   name
    "?sortorder",            # (6)   desc
    "?limit",                # (7)   42
    "?offset",               # (8)   24
]

parameter = ""
dataSpec = "="
params = input("Would you like to add any parameters?")

while params[0] == "y":
    if params == "yes":
        param1 = input("Which parameter?" '\n'
                       "    Data Type," '\n'
                       "    Location ID," '\n'
                       "    Station ID," '\n'
                       "    Start Date," '\n'
                       "    End Date," '\n'
                       "    Sort Field," '\n'
                       "    Sort Order," '\n'
                       "    Limit," '\n'
                       "    Offset")
        param1.lower()

        if param1.__contains__("data type"):
            dataSpec = dataSpec + input("Enter ID (Example - ACMH):")
            parameter = dataTypeParam[0] + dataSpec
            params = input("Would you like to add another?")

        elif param1.__contains__("location id"):
            dataSpec = dataSpec + input("Enter ID (Example - FIPS:37):")
            parameter = dataTypeParam[1]
            params = input("Would you like to add another?")

        elif param1.__contains__("station id"):
            dataSpec = dataSpec + input("Enter ID (Example - COOP:010957):")
            parameter = dataTypeParam[2]
            params = input("Would you like to add another?")

        elif param1.__contains__("start date"):
            dataSpec = dataSpec + input("Enter ID (Example - 1970-10-03):")
            parameter = dataTypeParam[3]
            params = input("Would you like to add another?")

        elif param1.__contains__("end date"):
            dataSpec = dataSpec + input("Enter ID (Example - 2012-09-10):")
            parameter = dataTypeParam[4]
            params = input("Would you like to add another?")

        elif param1.__contains__("sort field"):
            dataSpec = dataSpec + input("Enter ID (Example - name):")
            parameter = dataTypeParam[5]
            params = input("Would you like to add another?")

        elif param1.__contains__("sort order"):
            dataSpec = dataSpec + input("Enter ID (Example - desc):")
            parameter = dataTypeParam[6]
            params = input("Would you like to add another?")

        elif param1.__contains__("limit"):
            dataSpec = dataSpec + input("Enter ID (Example - 42):")
            parameter = dataTypeParam[7]
            params = input("Would you like to add another?")

        elif param1.__contains__("offset"):
            dataSpec = dataSpec + input("Enter ID (Example - 24):")
            parameter = dataTypeParam[8]
            params = input("Would you like to add another?")

        else:
            break