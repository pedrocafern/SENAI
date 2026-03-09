peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))

imc = peso / (altura ** 2)
print(f"O seu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Você está abaixo do peso.")
elif 18.5 <= imc < 25:
    print("Você está com o peso normal.")
elif 25 <= imc < 30:
    print("Você está com sobrepeso.")
elif 30 <= imc < 35:
    print("Você está com obesidade grau 1.")
elif 35 <= imc < 40:
    print("Você está com obesidade grau 2.")
else:    
    print("Você está com obesidade morbida.")