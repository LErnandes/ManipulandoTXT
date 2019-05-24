try:
    arquivo = open('teste.txt', 'r+')
    # Ele vai tentar ler o arquivo
except FileNotFoundError:
    # Se o arquivo não existir
    arquivo = open('teste.txt', 'w+')
    # Ele irá criar

# Daqui em diante você coloca o que você quiser fazer com o arquivo
arquivo.close()
