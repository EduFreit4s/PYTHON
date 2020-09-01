# ===================================
#  = https://github.com/EduFreit4s =
# ===================================

# ALGORITMO DE EXPANSÃO BINOMIAL DE NEWTON

# (x ± y)ⁿ >>>>>> Σₖⁿ (n!/k!*(n-k)!).(xₙ₋ₖ).(yₖ) [k=0] e [k<=n] 

def binomioNewton(X, Sinal, Y, e):
   
    k = 0

    def n_k(n, k):                              #DEFINIÇÃO DA SERIE DE NEWTON, O ESCALAR QUE MULTIPLICA X e Y
        numerador = factorial(n)
        denominador = factorial(k) * factorial(n-k) 
        return int(numerador/denominador)
    
    def factorial(n):
        if n < 0:
            return n
        elif n < 2:
            return 1
        else:
            return n * factorial(n-1)

    def expoenteUnicode(numero):                #RETORNA CARACTERE SOBRESCRITO
        return {                   
            1 : '¹', 2 : '²', 3 : '³', 4 : '⁴', 5 : '⁵', 6 : '⁶', 7 : '⁷', 8 : '⁸', 9 : '⁹', 0 : '°',
        }[numero] 
    
    def expoenteFlow(n):                        #CONCATENA AS UNIDADES DO EXPOENTE
        temp = str(n) 
        flow = ""
        for char in temp:
                flow += expoenteUnicode(int(char))
        return flow
            
    def sinalPotencia(signal, k):               #DEFINE O SINAL DO ESCALAR COM BASE NA PARIDADE DA POTÊNCIA
        if signal == "-":
            if k%2 != 0:
                return "-"
            else:
                return "+"
        elif signal == "+":
            return "+"
        else:
            return " Operador inválido "

    def fator(x, signal, y, n, k):              #CRIA OS PRODUTOS DA SOMA >> SINAL, VARIAVEL, EXPOENTE, VARIAVEL, EXPOENTE
        flow = ""
        if k <= n and k > 0:
            flow += str(sinalPotencia(signal, k))
        if n_k(n,k) > 1: 
            flow += str(n_k(n,k))
        if n-k > 0:
            flow += str(x)
        if n-k > 1:
            flow += expoenteFlow(n-k)
        if k > 0:
            flow += str(y)
        if k > 1:
            flow += expoenteFlow(k)
        return flow 

    formula = "(" + str(X)+str(Sinal)+str(Y) + ")" + expoenteFlow(e) + " = "

    if e > 0:                                   #CONCATENA OS PRODUTOS SEGUINDO A DEFINIÇÃO DA SERIE ENQUANTO K <= EXPOENTE
        while k <= e:
            formula += fator(X, Sinal, Y, e, k)
            k = k+1
    else: 
        formula += "Page not found"

    return formula

# TESTE
#print('\n' + binomioNewton("x","+","y",257) + '\n')       
       