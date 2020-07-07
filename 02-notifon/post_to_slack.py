import requests

url = 'https://hooks.slack.com/services/....' # Replace with Slack webhook URL
data = {"text": "Hello, world."}

requests.post(url, json=data)
