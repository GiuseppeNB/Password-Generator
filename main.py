import random

print("Bem-Vindo ao Gerador de Senhas")

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$¨&*().,?0123456789"

number = int(input("Quantidade de senhas para gerar: "))

length = int(input("Digite a quantidade de caracteres para a senha: "))

print("\nAqui estão as suas senhas:")

for pwd in range(number):
    passwords = ""
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)