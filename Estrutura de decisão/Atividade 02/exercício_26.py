try:
  comb = str(input("Escolha qual o tipo de combustível que deseja abastecer digitando: \n \nA - Álcool. \nG - Gasolina. \n \nOpção: "))
  comb == "A" or comb == "G"

  litros = float(input("\nAgora informe a quantidade de litros desejada: "))
  litros > 0
  
except:
  print("Digite os dados corretamente e tente novamente.")

try:
  if comb == "A":
    if litros > 20:
      