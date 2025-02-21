import webbrowser
llkk = []
čsl = [2, 1, 5, 3, 4, 9, 8, 6, 7]
pohlaví = "nevím "
ls = input("ahoj s čím chceš pomoci? ")
while True:
     if ls.lower() == 'kdo tebe naprogramoval':
        ls = input("naprogramoval mě jakub unger (ne ten novinář) ")
     elif ls.lower() == 'jaký je tvůj program':
           ls = input("můj program je z pythonu ")
     elif ls.lower() == 'ahoj':
           ls = input("ahoj s čím chceš pomoci? ")
     elif ls == 'mám tě ráda':
         pohlaví = "holka "
         ls = input("já taky❤️❤️❤️ ")
     elif ls == 'mám tě rád':
         pohlaví = "kluk "
         ls = input("já taky❤️❤️❤️ ")
     elif ls == 'jaké mám pohlaví':
         ls = input("jsi " + pohlaví)
     elif ls == 'co mám rád':
         if llkk == '[ ]':
           ls == input("nevím co máš rád? ")
           pohlaví = "kluk "
           llkk.append(ls)
         else:
              ls = input(f"máš rád {llkk} a něco jiného? ")
              llkk.append(ls)
              ls = input("ok ")
              pohlaví = "kluk "
     elif ls == 'co mám ráda':
          if llkk == '[ ]':
           ls == input("nevím co máš ráda? ")
           pohlaví = "holka "
           llkk.append(ls)
          else:
              ls = input(f"máš ráda {llkk} a něco jiného? ")
              llkk.append(ls)
              ls = input("ok ")
              pohlaví = "holka "
     elif ls == 'smaž to':
         llkk.pop()
         ls = input("mažu ")
     elif ls == 'čsl':
         ls = input(f"{čsl} ")
     elif ls == 'kkl':
         čsl.sort()
         ls = input(f"{čsl} ")
     elif ls == "otevři":
         gigh = input("co? ")
         url = gigh
         webbrowser.open(gigh)
         ls = input("hotovo ")
     elif ls == 'vypočítej':
          kpop = input("+ nebo - ? ")
          kpol = input("1 číslo? ")
          kpot = input("2 číslo? ")
          kpol = int(kpol)
          kpot = int(kpot)
          if kpop == '+':
