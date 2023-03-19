mlr_comp = "nenhum"
mlr_salto = 0.0
masv = 0.0
controle = "SIM"
while controle == "SIM" or controle == "S":
    # pegando dados
    competidor = input("qual o nome do atleta").upper()
    p1 = float(input("qual a distancia do primeiro salto"))
    p2 = float(input("qual a distancia do segundo salto"))
    p3 = float(input("qual a distancia do terceiro salto"))
    p4 = float(input("qual a distancia do quarto salto"))
    p5 = float(input("qual a distancia do quinto salto"))
    # estruturas de decisão maior/menor
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
        menor_salto = p3
    if p4 < mns:
        menor_salto = p4
    if p5 < mns:
        mns = p5
    # calculo da média dos saltos
    smedia = ((p1 + p2 + p3 + p4 + p5) - (mns + mas)) / 3
    # imprimindo informaçoes dos candidatos
    print(f"atleta {competidor}\n")
    print(f"primeiro salto -> {p1}")
    print(f"segundo salto -> {p2}")
    print(f"terceiro salto -> {p3}")
    print(f"quarto salto -> {p4}")
    print(f"quinto salto -> {p5}\n")
    print(f"o maior salto foi -> {mas}")
    print(f"o menor salto foi -> {mns}")
    print(f"a média dos saltos foi -> {smedia}")
    # continuar inserindo dados
    controle = input("deseja continuar inserindo competidores?").upper()
    # teste de qual foi o mlr competidor
    if smedia > mlr_salto:
        mlr_comp = competidor
        mlr_salto = smedia
        masv = mas
    if smedia == mlr_salto:
        if mas > masv:
            mlr_comp = competidor
            mlr_salto = smedia
# mostrando o melhor competidor
print(f"resultado final:\n{mlr_comp} -> {mlr_salto}")
