import requests

# Specify the correct API endpoint for cat facts
api_url = 'https://cat-fact.herokuapp.com/facts/random'

# Make the API request
response = requests.get(api_url)

if response.status_code == 200:
    try:
        # Parse and print the response data (e.g., cat facts)
        data = response.json()
        print(data)
    except Exception as e:
        print(f"Error parsing JSON data: {e}")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")