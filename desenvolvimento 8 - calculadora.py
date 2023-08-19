def calculadora(numero1, numero2, operacao):
    if operacao == 1:  # Soma
        resultado = numero1 + numero2
    elif operacao == 2:  # Subtração
        resultado = numero1 - numero2
    elif operacao == 3:  # Multiplicação
        resultado = numero1 * numero2
    elif operacao == 4:  # Divisão
        if numero2 != 0:
            resultado = numero1 / numero2
        else:
            print("Erro: Divisão por zero não é permitida.")
            return None
    else:
        print("Operação não reconhecida. Resultado definido como 0.")
        return 0
    
    return resultado
