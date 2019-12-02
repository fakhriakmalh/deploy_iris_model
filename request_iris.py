import requests
import json

# URL
url = 'http://127.0.0.1:5000/api'

# Change the value of experience that you want to test
payload = {
    'SepalLengthCm': 5.4, 
    'SepalWidthCm': 3.9, 
    'PetalLengthCm': 1.7, 
    'PetalWidthCm': 0.35}

#r = requests.post(url = url,data=payload)
#print(r.text)
data = json.dumps(payload)
send_request = requests.post(url, data)
print(send_request.json())
