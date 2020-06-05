import requests 

KEY = "bc5f3c4ea12f8a20f5d49ba45071ac67" 

def craft_url(city, key):
	url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"
	return url
   
def get_data(url):

        req = requests.get(url)
        data = req.json()
        return data
  
def get_city():
	city = input()
	return city
 
while True:
  
	print("[+] Input city")
	city = get_city()
	url = craft_url(city, KEY)
	print("[+] Getting data...")
	data = get_data(url)
	print(data)
