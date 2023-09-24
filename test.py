import requests

# Define the base URL of your Flask application
base_url = 'http://localhost:5000/here'  # Change this URL if your app is hosted elsewhere

# Define the endpoint URL for the specific CSV file you want to retrieve
file_url = f'{base_url}/file1/'  # Replace 'file1' with 'file2' or 'file3' as needed

# Function to make a request to the API and print the JSON response
def request_and_print(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print(f"Error: {response.status_code}")

# Make a request to the specified API endpoint
request_and_print(file_url)
