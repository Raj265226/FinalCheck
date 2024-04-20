import requests
response = requests.get("http://api.open-notify.org/iss-now.json")
print(response.json())
print(response.status_code)

My_Lat = 22.578590
My_long = 88.310850
parameters = {"lat":My_Lat, "lng":My_long,"date":"today"}
response1 = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
print(response1.json())
