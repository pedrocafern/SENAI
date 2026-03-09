x1 = float(input("Digite o valor de x1: "))
x2 = float(input("Digite o valor de x2: "))

opcao = input("Digite a opção desejada: Multiplicação (M), Divisão (D), Adição (A), Subtração (S) ")

match opcao:
    case "M":
        resultado = x1 * x2
        print(f"O resultado da multiplicação é: {resultado}")
    case "D":
        resultado = x1 / x2
        print(f"O resultado da divisão é: {resultado}")
    case "A":
        resultado = x1 + x2
        print(f"O resultado da adição é: {resultado}")
    case "S":
        resultado = x1 - x2
        print(f"O resultado da subtração é: {resultado}")
    case _:
        print("Opção inválida. Por favor, escolha M, D, A ou S.")