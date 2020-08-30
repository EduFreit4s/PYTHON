# ===================================
#  = https://github.com/EduFreit4s =
# ===================================

# CALCULA RESISTOR NECESSÁRIO PARA NÃO QUEIMAR O LED
# OBS: UNIDADE DE SAÍDA OHM
# VCC - TENSÃO DE ALIMENTAÇÃO
# VLED - TENSÃO DO LED

def resistorLed(vcc, vled):
    return int((vcc - vled) / 0.02)

# TESTE
#print(str(resistorLed(4, 3.15)) + " Ω")