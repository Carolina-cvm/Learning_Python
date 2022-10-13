sibilou = input("A criança já sibilou uma vez na vida?")

if sibilou == "sim" or sibilou == "Sim" or sibilou == "s":
  idade = input("A idade da criança é maior ou igual a 3 anos?")
  if idade == "sim" or idade == "Sim" or idade == "s":
    print("Provavelmente NÃO é asma induzida por vírus. Provável asma atópica, encaminhar ao especialista para iniciar tratamento preventivo.")
  else:
    criterio = input("A criança apresenta ao menos um dos critérios maiores?\n")
    if criterio == "sim" or criterio == "Sim" or criterio == "s":
      criteriomenos3x = input("Sibilou menos que 3x ao dia? (Dois episódios no total).\n")
      if criteriomenos3x == "sim" or criteriomenos3x == "Sim" or criteriomenos3x == "s":
        print("Provavelmente NÃO é asma induzida por vírus. Provável asma atópica de início recente, encaminhar ao especialista para verificar necessidade de tratamento preventivo no futuro.")
      else:
        print("Provavelmente NÃO é asma induzida por vírus. Provável asma atópica estabelecida, encaminhar ao especialista para acompanhar e iniciar tratamento preventivo.")
    else:
      naoapresentacriterio = input("A criança não apresenta critérios menores?\n")
      if naoapresentacriterio == "sim" or naoapresentacriterio == "Sim" or naoapresentacriterio == "s":
        naoapresentacriteriovezes = input("Sibilou menos que 3x ao dia? (Dois episódios no total).\n")
        if naoapresentacriteriovezes == "sim" or naoapresentacriteriovezes == "Sim" or naoapresentacriteriovezes == "s":
          print("Provavelmente É asma induzida por vírus. Acompanhá-la periodicamente, não necessita iniciar o tratamento preventivo.")
        else:
          print("Provavelmente É asma induzida por vírus. Acompanhá-la periodicamente, com eventos frequentes a decisão é individual pelo início do tratamento preventivo.")
      else:
          apresentaumcriterio = input("A criança apresenta ao menos um dos critérios menores?\n")
          if apresentaumcriterio == "sim" or apresentaumcriterio == "Sim" OR apresentaumcriterio == "s":
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
