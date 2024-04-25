import requests

'''
Requests é uma biblioteca Python que fornece uma interface simples e elegante para 
fazer solicitações HTTP. Ela é muito popular entre desenvolvedores web e de APIs, 
pois permite enviar e receber dados de servidores HTTP de forma rápida e fácil.
'''

try:
    # Faz uma requisição para o Google
    requests.get('https://www.google.com.br/', timeout=5)
    print("Conectado à internet!")
except requests.ConnectionError:
    # Se a requisição falhar, retorna False
    print("Sem conexão com a internet.")
    