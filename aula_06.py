import requests
import json
# site
url = 'https://pokeapi.co/api/v2/pokemon/bulbasaur'

# requisição
response = requests.request("GET", url)
print()

# Status 
print(response.status_code)
print("\n<===============================================>\n")

# variável guarda requisição em extensão JSON
req = response.json()
# imprimir dados

for n, i in enumerate(req, start=1):
    print(f'{n}ª chave:',i)
print("\n<===============================================>\n")

print('id =', req['id'])
print('nome =', req['name'])
