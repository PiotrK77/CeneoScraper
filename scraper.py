import requests



product_code = "133748381"        #input("Please enter product code: ")

print(product_code)

url = f"https://www.ceneo.pl/{product_code}#tab=reviews"
response = requests.get(url)
print(response.status_code)