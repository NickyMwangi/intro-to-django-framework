import requests
import endpoints

get_prod_by_id = requests.get(endpoints.prodById)
get_list_products = requests.get(endpoints.listProducts)

print(get_prod_by_id.json())
print(get_list_products.json())
