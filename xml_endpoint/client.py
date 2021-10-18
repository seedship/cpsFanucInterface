# importing the requests library
import requests
import time

# api-endpoint
URL = "http://127.0.0.1/KAREL/appmonitor"

# defining a params dict for the parameters to be sent to the API
PARAMS = {}

start = time.perf_counter()
# sending get request and saving the response as response object
r = requests.get(url=URL, params=PARAMS)
# extracting data in json format
data = r.json()
print(f"Completed Execution in {time.perf_counter() - start} seconds")

# extracting latitude, longitude and formatted address
# of the first matching location

print(data)