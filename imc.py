peso = float(input("Digite seu peso(em kg):"))
altura = float(input("Difgite sua altura(em metro, ex: 1.75):"))

imc = peso / (altura ** 2)
print(f"Seu imc é:{imc:.2f}")

if imc < 18.5:
    print("classificação: Abaixo")

elif imc < 25.0:
    print("classificação: Normal")

else:
    print("classificação: Obesidade")
    