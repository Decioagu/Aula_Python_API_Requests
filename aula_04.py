import requests
import json
# site
url = "https://pokeapi.co/api/v2/pokemon/"

# requisição
response = requests.request("GET", url)
print()

# Status 

print(response.status_code)
print("\n<===============================================>\n")



# variável guarda requisição em extensão JSON
req = response.json()
# imprimir dados
print(req['results'][0])
