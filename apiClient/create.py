import requests
import endpoints

data = {
  "title": "24 inch Monitor 4k",
  "description": "1920*1080 resolution and 165Hz",
  "price": 36525.00
}

update_data = {
  'pk': 6,
  "title": "Mosquito Killer",
  "description": "kills Mosquito",
  "price": 1225.23
}

create_Product = requests.post(endpoints.productCreate, json=data)
list_create_Product = requests.post(endpoints.listCreateProducts, json=data)
update_Product = requests.put(endpoints.productUpdate, json=update_data)
delete_Product = requests.delete(endpoints.productDelete)

print(create_Product.json())
print(list_create_Product.json())
print(update_Product.json())
print(delete_Product.json())
