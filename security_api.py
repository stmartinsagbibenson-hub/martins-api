import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("ABUSEIPDB_KEY")

ip_address = input("Enter your ip address: ")

url = "https://api.abuseipdb.com/api/v2/check"
querystring = {
    'ipAddress': ip_address,
    'maxAgeInDays': '90'
}
headers = {
    'Accept': 'application/json',
    'Key': api_key,
}

try:
    response = requests.request(method='GET', url=url, headers=headers, params=querystring)
except Exception as e:
    print(f"Error: {e}")

result = response.json()

with open("ip.json", "w") as file:
    json.dump(result, file, indent=4)

data = result["data"]

message = (
    f"\nThe ip address you provided: {ip_address} has an ip version of {data["ipVersion"]} "
    f"\nand is connected to the domain {data["domain"]} "
    f"and the abuse confidence score is {data["abuseConfidenceScore"]}."
)
with open("ip.txt", "w") as f:
    f.write(message)






