import requests

port = "8000"
endpoint = f"http://localhost:{port}/api/" # http://127.0.0.1:8000/

response = requests.get(endpoint, params={"abc": 123}, json={"hello":"world", "goat":"casperino7"})

code = response.status_code

print(response.json()) 
print("")
print(code)