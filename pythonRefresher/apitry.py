import requests

#try with agify api , no api key required

#url/ednpoint and params to send the query with what we want to ask
url = "https://api.agify.io"
params = {"name":"gunnika"}

#get request
response = requests.get(url, params=params)

print(response.status_code)

#convert to dictionary
data = response.json()

print(data)

#post request; sent with header(your api key and file format) and payload(your actual content)
url2 = "https://jsonplaceholder.typicode.com/posts"
headers = {"Content-Type": "application/json"}
payload = {
    "title": "Day 2 Practice",
    "body": "Learning POST requests in Python",
    "userId": 1
}
response2 = requests.post(url2, headers = headers, json = payload)
print(response2.status_code)
print(response2.json())

#api key is stored in .env file with exact format as KEYNAME=keyhere
#make a .gitignore and add .venv/ and .env there so it never gets added
# to load api key from .env
import os
from dotenv import load_dotenv
load_dotenv()
apikey = os.getenv("GRADIUM_API_KEY")
if not apikey:
    raise ValueError("api not found")

#for others you make a .env.example file which is similar to .env and not hidden in .gitignore