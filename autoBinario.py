# ===================================
#  = https://github.com/EduFreit4s =
# ===================================

# CONVERTE BASES BINÁRIO E DECIMAL 

def binarioDecimal(value):
    temp = str(value)
    bin = True
    
    def dec2Bin(decimal):                       #FAZ DIVISÕES SUCESSIVAS POR 2 E COLETA O RESTO. INVERTE A STRING COM [::-1]
        binario = ""
        while decimal != 0:
            binario += str(decimal%2)
            decimal = int(decimal/2)
        return binario[::-1]
    
    def bin2Dec(binario):                       #NOTAÇÃO POSICIONAL PARA CALCULAR CADA ELEMENTO E DEPOIS SOMAR
        bin = str(binario)
        bin = bin[::-1]
        indice = len(bin)-1
        decimal = 0
        while indice >= 0:
            decimal += 2**indice * int(bin[indice]) 
            indice -= 1           
        return str(decimal)

    for char in temp:                           #VERIFICA SE A ENTRADA É APENAS DECIMAL, SE SIM, SAÍDA APENAS BINÁRIO
        if int(char) > 1:
            bin = False
            break 

    if bin:
        return "Binário: " + dec2Bin(value) + '\n' + "Decimal: " + bin2Dec(value)
    else:
        return "Binário: " + dec2Bin(value) 

#TESTE
print("\n"+binarioDecimal(11)+"\n")