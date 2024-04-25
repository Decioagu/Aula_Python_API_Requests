import requests
import datetime

# Data do calendário atual "hoje"
data = datetime.datetime.now().strftime("%d\\%m\\%Y") #strftime("%Y-%m-%d %Hh:%Mm:%Ss")

url = 'https://api.exchangerate-api.com/v6/latest'

# Requisição
req = requests.get(url)

# Status da requisição
print(req.status_code)

# Variável guarda requisição em extensão JSON
dados = req.json()

# Exibir data de hoje e dados especifico da requisição 
print(f"\nO valor do \"U$\":dollar hoje {data} é de R$:{dados['rates']['BRL']}")