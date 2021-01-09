import requests
import json

base_url = "http://httpbin.org"

def get_delay(seconds):
    endpoint = f"/delay/{seconds}"
    print(f"Getting with {seconds} delay ...")
    
    response = requests.get(base_url+endpoint)
    data = response.json()
    print(json.dumps(data, indent=2))
    
get_delay(6)
print(f"Okay! All finished getting. ")