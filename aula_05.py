import requests

# site
url = "https://pokeapi.co/api/v2/pokemon/"

while url != None:

    # requisição
    response = requests.request("GET", url)
    print()

    # Status 
    print(response.status_code)
    print("\n<===============================================>\n")
   
    # variável guarda requisição em extensão JSON
    req = response.json()

    # imprimir dados
    for n, i in enumerate(req['results'], start=1):
        print(f'Lista de Pokemon {n}º => {i}')

    url = req["next"]

