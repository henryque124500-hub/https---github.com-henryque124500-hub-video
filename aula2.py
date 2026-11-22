nota1 = float(input("Digite a  sua primeira nota"))
nota2 = float(input("Digite a sua segunda nota"))

media = (nota1 + nota2) / 2
print(f"Média: {media:.1f}")

if media  >= 7.0:
    print("Situação: aprovado.")

elif media >= 5.0:
    print("Situação: recuperação")

else:
    print("Situação: voce esta reprovado.")


