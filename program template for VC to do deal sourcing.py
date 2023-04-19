#template for using python to do deal sourcing

import requests
import json

# Set up your API credentials and parameters
api_key = "YOUR_API_KEY"
search_query = "YOUR_SEARCH_QUERY"
base_url = "https://api.crunchbase.com/v3.1/odm-organizations"

# Make the API request
response = requests.get(
    url=base_url,
    params={
        "user_key": api_key,
        "q": search_query,
        "sort_order": "created_at DESC"
    }
)

# Parse the response JSON
data = json.loads(response.text)

# Extract relevant information from the response
for item in data['data']['items']:
    name = item['properties']['name']
    description = item['properties']['short_description']
    website = item['properties']['homepage_url']
    funding_rounds = item['relationships']['funding_rounds']['paging']['total_items']

    # Do further analysis or filtering on the extracted data here
    # ...

    # Print out the results
    print(f"Name: {name}")
    print(f"Description: {description}")
    print(f"Website: {website}")
    print(f"Funding rounds: {funding_rounds}")
    print("-----")
