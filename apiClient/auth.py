import requests
import endpoints
from getpass import getpass

password = getpass()

auth_response = requests.post(endpoints.auth, json={"username": "staff", "password": password})

print(auth_response.json())

if auth_response.status_code == 200:
  token = auth_response.json()['token']
  headers = {
    "Authorization": f"Bearer {token}"
  }
  get_products = requests.get(endpoints.listProducts, headers=headers)
  print(get_products.json())
