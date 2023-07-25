import requests
import endpoints

get_response = requests.get(endpoints.home)
get_product = requests.get(endpoints.product)
get_products = requests.get(endpoints.products)

print(get_response.text)
print(get_response.status_code)
print(get_response.json())
print(get_product.json())
print(get_products.json())
