def calculadora(numero1, numero2, operacao):
    if operacao == 1:  
        resultado = numero1 + numero2
    elif operacao == 2:  
        resultado = numero1 - numero2
    elif operacao == 3:  
        resultado = numero1 * numero2
    elif operacao == 4:  
        if numero2 != 0:
            resultado = numero1 / numero2
        else:
            print("Erro: Divisão por zero não é permitida.")
            return None
    else:
        print("Operação não reconhecida. Resultado definido como 0.")
        return 0
    
    return resultado

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
op = int(input("Digite o número da operação (1 para Soma, 2 para Subtração, 3 para Multiplicação, 4 para Divisão): "))

resultado = calculadora(num1, num2, op)
if resultado is not None:
    print("Resultado:", resultado)
