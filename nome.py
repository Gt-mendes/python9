# Entrada do usuário
nome = input("Digite seu nome completo: ")

print(f"\nNúmero de caracteres do seu nome: {len(nome)}")
print(f"Primeira letra: {nome[0]}")
print(f"Última letra: {nome[-1]}")
nome_completo = nome.upper()
print(f"Nome Maiúsculo: {nome_completo}")