mlr_comp = 'nenhum'
mlr_salto = 0.0
masv = 0.0
controle = 'SIM'

while controle == 'SIM' or controle == "S":

    competidor = input('qual o nome do atleta \n>>>').upper()
    while competidor.isalpha() == False:
        competidor = input(' Resposta invalida, tente digitar o somente o nome do atleta \n>>>').upper()

    p1 = input('qual a distancia do primeiro salto \n >>>')
    while p1.isnumeric() == False:
        p1 = input('resposta invalida \nqual a distancia do primeiro salto:\n>>> ')
    p1 = float(p1)

    p2 = input('qual a distancia do segundo salto \n>>>')
    while p2.isnumeric() == False:
        p2 = input('resposta invalida \nqual a distancia do segundo salto:\n>>> ')
    p2 = float(p2)

    p3 = input('qual a distancia do terceiro salto \n>>>')
    while p3.isnumeric() == False:
        p3 = input('resposta invalida \nqual a distancia do terceiro salto:\n>>> ')
    p3 = float(p3)

    p4 = input('qual a distancia do quarto salto \n>>>')
    while p4.isnumeric() == False:
        p4 = input('resposta invalida \nqual a distancia do quarto salto:\n>>> ')
    p4 = float(p4)

    p5 = input('qual a distancia do quinto salto \n>>>')
    while p5.isnumeric() == False:
        p5 = input('resposta invalida \nqual a distancia do quinto salto:\n>>> ')
    p5 = float(p5)

    mas = p1
    if p2 > mas:
        mas = p2
    if p3 > mas:
        mas = p3
    if p4 > mas:
        mas = p4
    if p5 > mas:
        mas = p5

        mns = p1
    if p2 < mns:
        mns = p2
    if p3 < mns:
        mns = p3
    if p4 < mns:
        mns = p4
    if p5 < mns:
        mns = p5

    smedia = ((p1 + p2 + p3 + p4 + p5) - (mns + mas)) / 3

    print(f"atleta \n-> {competidor}\n")
    print(f"primeiro salto \n-> {p1}")
    print(f"segundo salto \n-> {p2}")
    print(f"terceiro salto \n-> {p3}")
    print(f"quarto salto \n-> {p4}")
    print(f"quinto salto \n-> {p5}\n")
    print(f"o maior salto foi \n-> {mas}")
    print(f"o menor salto foi \n-> {mns}")
    print(f"a média dos saltos foi \n-> {smedia}")

    if smedia > mlr_salto:
        mlr_comp = competidor
        mlr_salto = smedia
        masv = mas

    if smedia == mlr_salto:
        if mas > masv:
            mlr_comp = competidor
            mlr_salto = smedia

    controle = input("deseja continuar inserindo competidores?").upper()


print(f"resultado final:\n{mlr_comp} -> {mlr_salto}")
