import os
import json
import requests
from dotenv import load_dotenv
from rules import botscore_ruleset


load_dotenv()


# Define Cloudflare API credentials
api_key = os.getenv('API_KEY')
email = os.getenv('EMAIL')




# Common headers for Cloudflare API requests (For Authorization)
headers = {
    'X-Auth-Email': email,
    'X-Auth-Key': api_key,
    'Content-Type': 'application/json',
}

print(headers)

def apply_ruleset_to_zone(zone_id):
    url = f'https://api.cloudflare.com/client/v4/zones/{zone_id}/rulesets'
    
    # POST request to apply the ruleset
    response = requests.post(url, headers=headers, data=json.dumps(botscore_ruleset))
    
    if response.status_code == 200:
        print(f"Ruleset applied successfully to Zone ID: {zone_id}")
    else:
        print(f"Failed to apply ruleset to Zone ID: {zone_id}. Status Code: {response.status_code}")
        print("Response:", response.text)

# Main program to get the zone ID and apply the ruleset
def main():
    print("Welcome to the Cloudflare WAF Ruleset Application Program!")
    
    # Ask the user to input the zone ID
    zone_id = input("Please enter the Zone ID you wish to apply the ruleset to: ")
    
    # Apply the predefined ruleset to the provided zone ID
    print("\nApplying ruleset...")
    apply_ruleset_to_zone(zone_id)


if __name__ == "__main__":
    main()
