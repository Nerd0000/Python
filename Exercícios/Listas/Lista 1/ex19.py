def essaEtapa(PorESL, PorCEG, PorIVA):
    esl = 49
    lex = 30
    ceg = 19
    iva = 42
    ivc = esl+lex+ceg
    ava = ivc+iva
    mediaAVA = ava*0.6

    cEsl = esl*PorESL/100
    cCeg = ceg*PorCEG/100
    cIva = iva*PorIVA/100

    cLex = mediaAVA - cCeg - cEsl - cIva
    
    if cLex>60: print(cLex*100/lex, '%')
    else: print("Já passou")

essaEtapa(100, 100, 100)