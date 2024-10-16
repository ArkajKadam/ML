import json
import requests

api_key = "5a2079726df9da63a467b5825cc2429b"
city = "Sangli"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    print(json.dumps(data, indent=5))
    
    with open("weather_data.json","w") as file:
        json.dump(data,file,indent=5)
else: 
    print(f"Error : {response.status_code}")