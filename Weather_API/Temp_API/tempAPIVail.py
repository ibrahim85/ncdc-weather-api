import pycurl
from Weather_API.Temp_API import inputReader
from io import BytesIO

reader = inputReader

baseurl = "http://www.ncdc.noaa.gov/cdo-web/api/v2"

tokenParam = "sDDqnqqBmkfUFSEzXoElcgzmYrtTyZGz"

# Define URL That is Desired starting with url + endPoint[n]
finalUrl = baseurl + reader.main()
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