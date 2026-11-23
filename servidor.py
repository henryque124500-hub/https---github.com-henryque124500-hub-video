login = input("Digite seu login: ").strip().lower()
senha = input("Digite sua senha: ").strip().lower()

if login == 'carlos.silva' and senha == ("abc"):
    print("Acesso permitido!")

else:
    print("Login e/ou senha incorreta. Tente novamente!")

print()