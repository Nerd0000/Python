def necessidade(p1, p2):
    etapa1 = 110
    etapa2 = 140
    etapa3 = 150

    totalEtapas = etapa1 + etapa2 + etapa3
    mediaEtapas = totalEtapas*0.6

    yEtapa1 = etapa1*p1/100
    yEtapa2 = etapa2*p2/100
    yEtapa3 = mediaEtapas - yEtapa1 - yEtapa2

    print(100*yEtapa3/totalEtapas, '%')

print(necessidade(40, 70))