

def verificar_codigo(codigo):
  palavras_reservadas = keyword.kwlist
  delimitadores = ["(", ")", "[", "]", "{", "}", ".", ",", ":", ";"]
  strings = ["'", '"']
  operadores_logicos = ["and", "or", "not"]

  resultados = []
  for linha in codigo.split("\n"):
    linha_resultados = []
    for palavra in linha.split():
      if palavra in palavras_reservadas:
        linha_resultados.append("Palavra reservada: {}".format(palavra))
      elif palavra in delimitadores:
        linha_resultados.append("Delimitador: {}".format(palavra))
      elif palavra in strings:
        linha_resultados.append("String: {}".format(palavra))
      elif palavra in operadores_logicos:
        linha_resultados.append("Operador lógico: {}".format(palavra))
      else:
        linha_resultados.append("Outro: {}".format(palavra))
    resultados.append("Linha {}: {}".format(linhas.index(linha) + 1, ", ".join(linha_resultados)))
  return resultados

