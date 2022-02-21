import requests
import enchant 

with open("dicionario.txt", "r", encoding = "utf8") as f:
    linhas = f.readlines()
with open("dicionario5letras.txt", "w", encoding = "utf8") as f:
    for line in linhas:
        if len(line) == 6:
            f.write(line)