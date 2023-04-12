try:
  print("Respoda as perguntas com Sim ou Não. \n")
  perg1 = input("Telefonou para a vítima? ")
  perg2 = input("Esteve no local do crime? ")
  perg3 = input("Mora perto da vítima? ")
  perg4 = input("Devia para a vítima? ")
  perg5 = input("Já trabalhou com a vítima? ")
    
  if perg1 == "Sim":
    perg1 == 1
  else:
    perg1 == 0
    pass
    
  if perg2 == "Sim":
    perg2 == 1
  else:
    perg2 == 0
    pass
    
  if perg3 == "Sim":
    perg3 == 1
  else:
    perg3 == 0
    pass
    
  if perg4 == "Sim":
    perg4 == 1
  else:
    perg4 == 0
    pass
    
  if perg5 == "Sim":
    perg5 == 1
  else:
    perg5 == 0
    pass
    
  soma_perg = perg1 + perg2 + perg3 + perg4 + perg5
  
  match soma_perg:
    case 0:
      print("Inocente!")
    case 1:
      print("Inocente!")
    case 2:
      print("Supeita!")
    case 3:
      print("Cúmplice!")
    case 4:
      print("Cúmplice!")
    case 5:
      print("Assassino!")
except:
  print("Tente novamente respondendo Sim ou Não.")