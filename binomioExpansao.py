# ===================================
#  = https://github.com/EduFreit4s =
# ===================================

# ALGORITMO DE EXPANSÃO BINOMIAL DE NEWTON
# OBS : SAÍDA STRING, NÃO REALIZA CALCULO AINDA

def binomioExpansao(a, b, n):
    formula = ""
    k = 0

    def factorial(n):
        if n < 0:
            return n
        elif n < 2:
            return 1
        else:
            return n * factorial(n-1)

    def expoenteUnicode(numero):
        return {                   
            1 : '¹', 2 : '²', 3 : '³', 4 : '⁴', 5 : '⁵', 6 : '⁶', 7 : '⁷', 8 : '⁸', 9 : '⁹', 0 : '°',
        }[numero] 
    
    def expoente(n):
        temp = str(n)
        exp =""
        for char in temp:
                exp += expoenteUnicode(int(char))
        return exp
            
    def n_k(n, k):
        return int( factorial(n) / (factorial(k) * factorial((n-k))) )
    
    def makePolinomio(x, y, n, k):
        expressao = ""
        if n_k(n,k) > 1: 
            expressao += str(n_k(n,k))
        if n-k > 0:
            expressao += str(x)
        if n-k > 1:
            expressao += expoente(n-k)
        if k > 0:
            expressao += str(y)
        if k > 1:
            expressao += expoente(k)
        if k < n:
            expressao += "+"
        return expressao 

    if n > 0:
        while k <= n:
            formula += makePolinomio(a, b, n, k)
            k = k+1
    else: 
        formula += "Page not found"


    return formula

# TESTE
#print('\n' + binomioExpansao("x","y",42) + '\n')
        
       