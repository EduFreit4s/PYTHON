# ===================================
#  = https://github.com/EduFreit4s =
# ===================================

# TRADUZ CÓDIGO DE CORES DE RESISTORES DE QUATRO BANDAS
# OBS : SAÍDA STRING

def resistorCor(cor1, cor2, cor3, cor4):    
    
    def corToNumber(cor):           # CONVERTE COR DO PARAMETRO PARA NUMERO 
        return {                    # TIPO DICIONÁRIO (gambiarra parecida com switch rs)
            "PRETO" : 0,
            "MARROM" : 1,
            "VERMELHO" : 2,
            "LARANJA" : 3,
            "AMARELO" : 4,
            "VERDE" : 5,
            "AZUL" : 6,
            "VIOLETA" : 7,
            "CINZA" : 8,
            "BRANCO" : 9,
            "OURO" : -1,
            "PRATA" : -2
        }[cor.upper()]              # upper() CONVERTE TODA LETRA PARA CAIXA ALTA 

    def tolerancia(cor4):           #USA DINICONÁRIO PARA VERIFICAR AS TOLERÂNCIAS 
        if corToNumber(cor4) == 2:
            return " ±2%"
        elif corToNumber(cor4) == -1:
            return " ±5%"
        elif corToNumber(cor4) == -2:
            return " ±10%"
        else:
            return " ±20%"
    
    def prefixo(ohm):               # IMPLEMENTA O PREFIXO E REDUZ O NUMERO INICIALMENTE EM OHMS
        if ohm >= 1000000000:
            return str(int(ohm/1000000000))+" GΩ" + tolerancia(cor4)
        elif ohm >= 1000000:
            return str(int(ohm/1000000))+" MΩ" + tolerancia(cor4)
        elif ohm >= 1000:
            return str(int(ohm/1000))+" kΩ" + tolerancia(cor4)
        else:
            return str(ohm)+" Ω" + tolerancia(cor4)

    resistencia = (corToNumber(cor1)*10 + corToNumber(cor2)) * pow(10, corToNumber(cor3))
    return prefixo(resistencia)
        
# TESTE
#print(resistorCor("amarelo","vermelho", "preto", "ouro")) 