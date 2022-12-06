sibilou = input(f'A criança já sibilou uma vez na vida?')

if sibilou == "sim" or sibilou == "Sim" or sibilou == "s":
  idade = input(f'A idade da criança é maior ou igual a 3 anos?')
  if idade == "sim" or idade == "Sim" or idade == "s":
    print(f'Provavelmente NÃO é asma induzida por vírus. Provável asma atópica, encaminhar ao especialista para iniciar tratamento preventivo.')
  else:
    criterio = input(f'A criança apresenta ao menos um dos critérios maiores? ')
    if criterio == "sim" or criterio == "Sim" or criterio == "s":
      criteriomenos3x = input(f'Sibilou menos que 3x ao dia? (Dois episódios no total) ')
      if criteriomenos3x == "sim" or criteriomenos3x == "Sim" or criteriomenos3x == "s":
        print(f'Provavelmente NÃO é asma induzida por vírus. Provável asma atópica de início recente, encaminhar ao especialista para verificar necessidade de tratamento preventivo no futuro.')
      else:
        print(f'Provavelmente NÃO é asma induzida por vírus. Provável asma atópica estabelecida, encaminhar ao especialista para acompanhar e iniciar tratamento preventivo.')
    else:
      naoapresentacriterio = input(f'A criança não apresenta critérios menores?')
      if naoapresentacriterio == "sim" or naoapresentacriterio == "Sim" or naoapresentacriterio == "s":
        naoapresentacriteriovezes = input(f'Sibilou menos que 3x ao dia? (Dois episódios no total).')
        if naoapresentacriteriovezes == "sim" or naoapresentacriteriovezes == "Sim" or naoapresentacriteriovezes == "s":
          print(f'Provavelmente É asma induzida por vírus. Acompanhá-la periodicamente, não necessita iniciar o tratamento preventivo.')
        else:
          print("Provavelmente É asma induzida por vírus. Acompanhá-la periodicamente, com eventos frequentes a decisão é individual pelo início do tratamento preventivo.")
      else:
          apresentaumcriterio = input(f'A criança apresenta ao menos um dos critérios menores?')
          if apresentaumcriterio == "sim" or apresentaumcriterio == "Sim" OR apresentaumcriterio == "s":
              apresentaumcriteriovezes = input(f'Sibilou menos que 3x ao dia? (Dois episódios no total).')
              if apresentaumcriteriovezes == "sim":
                  print(f'Provavelmente É asma induzida por vírus. Acompanhá-la periodicamente, não necessita iniciar o tratamento preventivo.')
              else:
                print("Provavelmente É asma induzida por vírus. Acompanhá-la periodicamente, com eventos frequentes a decisão é individual pelo início do tratamento preventivo.")
          else:
            apresentadoiscriterios = input(f'A criança apresenta ao menos dois critérios menores?')
            if apresentadoiscriterios == "sim":
                apresentadoiscriteriosvezes = input("Sibilou menos que 3x ao dia? (Dois episódios no total).\n")
                if apresentadoiscriteriosvezes == "sim":
                    print("Provavelmente NÃO é asma induzida por vírus. Provável asma atópica, de início recente, encaminhar ao especialista, para verificar necessidade de tratamento preventivo no futuro.")
                else:
                    print("Provavelmente NÃO é asma induzida por vírus. Provável asma atópica estabelecida, encaminhar ao especialista para acompanhar e iniciar tratamento preventivo.")
            else:
                print(f'Não é asma induzida por vírus')  	
else: 
  print("Não é asma induzida por vírus")	    
