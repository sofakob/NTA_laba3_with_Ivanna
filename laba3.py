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
            return int(k), div
    return rivnain(alhpa, s, n)

def huba(alhpa:int, s:list, n:int, k:list, div:list):
    k2, div2=rivnain(alhpa, s, n)
    if k2 not in k:
            k.append(k2)
            div.append(div2)
        
    
    return k, div

def liniyno_nezalegn(k, div):
    k_for=k[:]
    div_for=div[:]
    matr=numpy.array([row +[k[i]] for i, row in enumerate(div)])
    matrixa=[row +[k[i]] for i, row in enumerate(div)]
    matr_without_linia=numpy.array(matrixa[0])
    matr_without_linia=numpy.array(matrixa[0:1])
    index1=numpy.linalg.matrix_rank(matr_without_linia, 0)
    for i in range(1, len(k_for)):
        matr_without_linia=numpy.array(matrixa[0:i+1])
        index2=numpy.linalg.matrix_rank(matr_without_linia, 1e-10)
        if index2==index1:
            matrixa.pop(i)
            k_for.pop(i)
            div_for.pop(i)
            i=-1
        index1=index2
    matr_without_linia=numpy.array(matrixa[:])
    
    return k_for, div_for
    


def index_calculus(alhpa:int, beta:int, n:int):
    c=3.38
    base=int(2)
    b=int(c*math.exp((1/2)*math.sqrt(math.log(n, base)*math.log(math.log(n, base), base))))
    s=list(sympy.primerange(2, b)) 
    print(s)

    k, div=rivnain(alhpa, s, n)
    k2, div2=rivnain(alhpa, s, n)
    while k==k2:
        k2, div2=rivnain(alhpa, s, n)
    k=[k, k2]
    div=[div, div2]
    print(k, div)
    reshenie=None
    i=0
    while reshenie is None:
        try:
            k, div=liniyno_nezalegn(k, div)
            matr=sympy.Matrix([row +[k[i]] for i, row in enumerate(div)])
            k_coef=[]
            for i in range(len(k)):
                k_coef.append("X"+str(i+1))

            reshenie = sympy.solve_linear_system_LU(matr, k_coef)
        except:
            reshenie=None
            k, div=huba(alhpa, s, n, k, div)
    #print(reshenie)

 

        
        
        



    A=numpy.array()
    








index_calculus(10, int(17), int(47))