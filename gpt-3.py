# A Python script to fetch data from the GPT-3 API using the OpenAI API
import requests

# Replace with your OpenAI API key
API_KEY = "YOUR_API_KEY"

# Set the API endpoint
ENDPOINT = "https://api.openai.com/v1/engines/gpt-3/jobs"

# Define the request data
data = {
    "model": "text-davinci-002",
    "prompt": "What is the capital of France?",
    "max_tokens": 2048,
    "n": 1,
    "stop": None,
    "temperature": 0.5,
}

# Send the request to the API
response = requests.post(ENDPOINT, json=data, headers={"Authorization": "Bearer " + API_KEY})

# Check the response status code
if response.status_code == 200:
    # Print the generated text
    print(response.json()["choices"][0]["text"])
else:
    # Print the error message
    print("Error: " + response.json()["message"])
