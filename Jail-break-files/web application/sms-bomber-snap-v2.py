# This new update can binding your ip with using tor 

import requests
import stem
from stem import Signal
from stem.control import Controller

# Set up TOR proxy
session = requests.session()
session.proxies = {'http': 'socks5://127.0.0.1:9050', 'https': 'socks5://127.0.0.1:9050'}

# Send request through TOR
def send_request():
    with Controller.from_port(port = 9051) as controller:
        controller.authenticate()
        controller.signal(Signal.NEWNYM)
    response = session.get('https://app.snapp.taxi/api/api-passenger-oauth/v2/otp')
    print(response.text)

# Send multiple requests
for i in range(10):
    send_request()
