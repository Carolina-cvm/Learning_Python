sibilou = input("A criança já sibilou uma vez na vida?\n")
if sibilou == "sim":
  idade = input("A idade da criança é maior ou igual a 3 anos?\n")
  if idade == "sim":
    print("Provavelmente NÃO é asma induzida por vírus. Provável asma atópica, encaminhar ao especialista para iniciar tratamento preventivo.")
  else:
    criterio = input("A criança apresenta ao menos um dos critérios maiores?\n")
    if criterio == "sim":
      criteriomenos3x = input("Sibilou menos que 3x ao dia? (Dois episódios no total).\n")
      if criteriomenos3x == "sim":
        print("Provavelmente NÃO é asma induzida por vírus. Provável asma atópica de início recente, encaminhar ao especialista para verificar necessidade de tratamento preventivo no futuro.")
      else:
        print("Provavelmente NÃO é asma induzida por vírus. Provável asma atópica estabelecida, encaminhar ao especialista para acompanhar e iniciar tratamento preventivo.")
    else:
      naoapresentacriterio = input("A criança não apresenta critérios menores?\n")
      if naoapresentacriterio == "sim":
        naoapresentacriteriovezes = input("Sibilou menos que 3x ao dia? (Dois episódios no total).\n")
        if naoapresentacriteriovezes == "sim":
          print("Provavelmente É asma induzida por vírus. Acompanhá-la periodicamente, não necessita iniciar o tratamento preventivo.")
        else:
          print("Provavelmente É asma induzida por vírus. Acompanhá-la periodicamente, com eventos frequentes a decisão é individual pelo início do tratamento preventivo.")
      else:
          apresentaumcriterio = input("A criança apresenta ao menos um dos critérios menores?\n")
          if apresentaumcriterio == "sim":
              apresentaumcriteriovezes = input("Sibilou menos que 3x ao dia? (Dois episódios no total).\n")
              if apresentaumcriteriovezes == "sim":
                  print("Provavelmente É asma induzida por vírus. Acompanhá-la periodicamente, não necessita iniciar o tratamento preventivo.")
              else:
                print("Provavelmente É asma induzida por vírus. Acompanhá-la periodicamente, com eventos frequentes a decisão é individual pelo início do tratamento preventivo.")
          else:
            apresentadoiscriterios = input("A criança apresenta ao menos dois critérios menores?\n")
            if apresentadoiscriterios == "sim":
                apresentadoiscriteriosvezes = input("Sibilou menos que 3x ao dia? (Dois episódios no total).\n")
                if apresentadoiscriteriosvezes == "sim":
                    print("Provavelmente NÃO é asma induzida por vírus. Provável asma atópica, de início recente, encaminhar ao especialista, para verificar necessidade de tratamento preventivo no futuro.")
                else:
                    print("Provavelmente NÃO é asma induzida por vírus. Provável asma atópica estabelecida, encaminhar ao especialista para acompanhar e iniciar tratamento preventivo.")
            else:
                print("Não é asma induzida por vírus")  	
else: 
  print("Não é asma induzida por vírus")	    
