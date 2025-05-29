import sympy
import math
import random
import numpy



def rivnain(alhpa:int, s:list, n:int):
    k=random.randint(0, n-1)
    a_k=pow(alhpa, k, n)
    div=[]
    for i in range(len(s)):
        if a_k%s[i]==0:
            div.append(1)
            a_k/=s[i]
            while a_k%s[i]==0:
                div[i]+=1
                a_k/=s[i]
        else:
            div.append(0)
    for i in range(len(div)):
        if div[i]!=0:
            return k, div
    return rivnain(alhpa, s, n)

def huba(alhpa:int, s:list, n:int, k:list, div:list):
    k2, div2=rivnain(alhpa, s, n)
    k.append(k2)
    div.append(div2)
    return k, div




def index_calculus(alhpa:int, beta:int, n:int):
    c=3.38
    base=int(2)
    b=c*math.exp((1/2)*math.sqrt(math.log(n, base)*math.log(math.log(n, base), base)))
    s=list(sympy.primerange(2, b)) 
    k, div=rivnain(alhpa, s, n)
    k2, div2=rivnain(alhpa, s, n)
    k=[k, k2]
    div=[div, div2]
    reshenie=None
    while reshenie==None:
        try:
            reshenie=numpy.linalg.solve(k, div)
        except:
            reshenie=None
            k, div=huba(alhpa, s, n, k, div)
        
        



    A=numpy.array()
    







index_calculus(1, 1, int(1000))