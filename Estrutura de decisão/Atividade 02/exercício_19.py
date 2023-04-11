try:
  num = int(input("Digite um número 1 à 999: "))
  if num < 0 or num > 999:
    print("O número deve estar entre 1 e 999. Tente novamente.")
  else:
    centena = num/100
    dezena = num/10
    unidade = num/1
    print(f"A quantidade de centenas desse número é de: {centena}. \nA quantidade de dezenas desse número é de: {dezena}. \nA quantidade de unidades desse número é de: {unidade}.")
except:
  print("Tente novamente. Digite um número.")