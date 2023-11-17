import requests
import json

# Define a URL da API da Mega Sena
URL = "https://servicebus2.caixa.gov.br/portaldeloterias/api/megasena"

# Faz a requisição à API
resposta = requests.get(URL)

# Converte a resposta em um objeto JSON
resultados = json.loads(resposta.content)

# Cria um array para armazenar os números repetidos
numeros_repetidos = []

# Itera sobre os resultados
for resultado in resultados:
    # Adiciona os números repetidos ao array
    for numero in resultado["numeros"]:
        if numero in numeros_repetidos:
            continue

        numeros_repetidos.append(numero)

# Gera um resultado novo com base nos números repetidos
resultado_novo = [
    numeros_repetidos[random.randint(0, len(numeros_repetidos) - 1)],
    numeros_repetidos[random.randint(0, len(numeros_repetidos) - 1)],
    numeros_repetidos[random.randint(0, len(numeros_repetidos) - 1)],
    numeros_repetidos[random.randint(0, len(numeros_repetidos) - 1)],
    numeros_repetidos[random.randint(0, len(numeros_repetidos) - 1)],
]

# Gera 10 resultados aleatórios
resultados_aleatorios = []
for i in range(10):
    resultados_aleatorios.append(random.randint(1, 60))

# Exibe o resultado novo
print("Resultado novo:", ",".join(resultado_novo))

# Exibe 10 resultados aleatórios
print("Resultados aleatórios:", ",".join(resultados_aleatorios))