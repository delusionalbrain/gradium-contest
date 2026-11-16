import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GRADIUM_API_KEY")

url = "https://api.example.com/v1/endpoint"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}
payload = {"text": "Hello world"}

try:
    # timeout=15 prevents your script from hanging forever if the server stalls
    response = requests.post(url, headers=headers, json=payload, timeout=15)
    
    # Immediately jumps to HTTPError if status code is 4xx or 5xx
    response.raise_for_status()
    
    result = response.json()
    print("Success:", result)

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP Error occurred: {http_err}")
    # CRITICAL: Always print response.text to see the API's exact explanation!
    print("Server Error Details:", response.text)

except requests.exceptions.Timeout:
    print("Request timed out. The server took too long to respond.")

except requests.exceptions.RequestException as err:
    print(f"Network/Connection error: {err}")