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
# imprimir dados como texto
print(response.text)
print("\n<===============================================>\n")


# variável guarda requisição em extensão JSON
req = json.loads(response.text)

# imprimir dados
# print(req)
for n, i in enumerate(req['results'], start=1):
    print(f'Lista de Pokemon {n}º => {i}')

'''
"Requests" é uma biblioteca Python popular que simplifica a criação de 
solicitações HTTP (como GET, POST, PUT, etc.) para servidores web.

Exemplo:
requests.request(method='GET', url='https://example.com', **kwargs)

Ele é usado para enviar uma solicitação HTTP para uma URL, com argumentos:
    # method (obrigatório): O método HTTP a ser usado (por exemplo, 'GET', 'POST', 'PUT', 'DELETE', etc.).
    # url (obrigatório): a URL do recurso da Web que você deseja acessar.
    # **kwargs (opcional): argumentos de palavra-chave adicionais para personalizar a solicitação:
        # headers (dict): Um dicionário de cabeçalhos para enviar com a solicitação.
        # data (dict ou bytes): Dados a enviar no corpo da solicitação (para POST, PUT, etc.).
        # json (dict): Dados a serem codificados em JSON e enviados no corpo da solicitação.
        # params (dict): Um dicionário de parâmetros de consulta para adicionar à URL.
        # auth (tupla): credenciais de autenticação (nome de usuário, senha) ou um objeto de autenticação personalizado.
        # cookies (ditado): Um dicionário de cookies para enviar com o pedido.
        # timeout (float): O número máximo de segundos para aguardar uma resposta.
'''

