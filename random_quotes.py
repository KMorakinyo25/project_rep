import requests

url = 'https://official-joke-api.appspot.com/jokes/random'
response = requests.post(url)

print(response.json())