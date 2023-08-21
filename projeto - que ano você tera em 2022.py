def ano_valido():
  executar = True
  while executar == True:
        try:
            ano = int(input("Digite o ano de nascimento (entre 1922 e 2021): "))
            if 1922 <= ano <= 2021:
                return ano
            else:
                print("Ano fora do intervalo válido. Tente novamente.")
        except:
            print("Valor inválido. Digite um número válido.")

def menu():
  nome = input("Digite seu nome completo: ")
  ano_nascimento = ano_valido()

  ano_atual = 2022
  idade = ano_atual - ano_nascimento

  print("nome:",nome)
  print("sua data de nascimento:",ano_nascimento)
  print("sua idade em 2022:", idade)

menu()  
