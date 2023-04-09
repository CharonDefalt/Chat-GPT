import requests
from bs4 import BeautifulSoup

url = input("Enter the URL of the web application to scan: ")

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

forms = soup.find_all('form')

for form in forms:
    action = form.get('action')
    method = form.get('method')
    inputs = form.find_all('input')

    for input in inputs:
        name = input.get('name')
        value = input.get('value')
        if value:
            value = value.strip()

        if method == 'get':
            params = {name: value}
            r = requests.get(url, params=params)
        elif method == 'post':
            data = {name: value}
            r = requests.post(url, data=data)

        if 'error' in r.text.lower():
            print(f"Vulnerability found in {action} with {method} method")
