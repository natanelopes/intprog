"""
Programa Adulto
Descrição: Este programa determina se o usuário é adulto.
Autor: Natane Fraga Lopes
Data: 20/02/2025
Versão: 0.0.1
"""

# Alocação de memória

idade = 0

frase = ""


# Entrada de dados

idade = int(input("Qual a sua idade: "))


# Processamento de dados

if idade > 18:
    frase = "Oi! Você é um adulto."


# Saída de dados

print(frase)

