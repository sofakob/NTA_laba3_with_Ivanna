import sympy
import math
import random
import numpy



def rivnain(alhpa:int, s:list, n:int):
    k=random.randint(0, 7)
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
    for j in range(1, len(k_for)):
        matr_without_linia=numpy.array(matrixa[0:j+1])
        index2=numpy.linalg.matrix_rank(matr_without_linia, 1e-10)
        if index2==index1:
            matrixa.pop(j)
            k_for.pop(j)
            div_for.pop(j)
            j=-1
        index1=index2
    matr_without_linia=numpy.array(matrixa[:])
    
    return k_for, div_for


def chetvertuykrok(alhpa:int, beta:int, s:list, n:int):
    k=random.randint(0, n-1)
    a_k_b=(pow(alhpa, k)*beta)%n
    div=[]
    for i in range(len(s)):
        if a_k_b%s[i]==0:
            div.append(1)
            a_k_b/=s[i]
            while a_k_b%s[i]==0:
                div[i]+=1
                a_k_b/=s[i]
        else:
            div.append(0)
    for i in range(len(div)):
        if div[i]!=0:
            return int(k), div
    return chetvertuykrok(alhpa, beta, s, n)

def poshuk_log(znachenie_log_x:list, d:list, l:int, n):
    n=n-1
    sum=0
    for i in range(len(znachenie_log_x)):
        sum+=d[i]*znachenie_log_x[i]

    log_alfa=(sum-l)%n
    return log_alfa




def algoritm_evklida_with_a_b(b:int, a:int, n:int):
    '''
    Алгоритм евкліда теж таблична реалізація, при цікавості можна вивести табличкою. Ця функція була переписана з того, що я писала на с++
    ще на першому курсі, але повертаємо тільки обернене
    а число за модулем якого ми шукаємо обернене
    b число для якого ми шукаємо обернене
    додатково є вимога що а та b повинні бути інтови, щоби випадково не було приколів
    '''
    a-=1
    n-=1
    if b>a:
        b%=a
    q=0
    u=1; v=0; u1=0; v1=1
    while a>b:
        c=a
        while c>b:
            c=c-b
            q+=1
        a=b; b=c
        u2=u-u1*q
        v2=v-v1*q
        u=u1; v=v1; u1=u2; v1=v2; q=0
        
    
    if v<0:
        v=n+v
    return v

def index_calculus(alhpa:int, beta:int, n:int):
    c=3.38
    base=int(2)
    b=int(c*math.exp((1/2)*math.sqrt(math.log(n, base)*math.log(math.log(n, base), base))))
    s=list(sympy.primerange(2, b))
    print(s) 
    s=[2, 3, 5, 7]
    k, div=rivnain(alhpa, s, n)
    k2, div2=rivnain(alhpa, s, n)
    while k==k2:
        k2, div2=rivnain(alhpa, s, n)
    k=[k, k2]
    div=[div, div2]
    reshenie=None
    i=0
    while reshenie is None and i<50:
        print(k, div, i)
        i=1+i
        try:
            k, div=liniyno_nezalegn(k, div)
            matr=sympy.Matrix([row +[k[j]] for j, row in enumerate(div)])
            k_coef=[]
            for j in range(len(k)):
                k_coef.append("X"+str(j+1))

            reshenie = sympy.solve_linear_system_LU(matr, k_coef)
        except:
            reshenie=None
            k, div=huba(alhpa, s, n, k, div)
    print(reshenie)
    chiselnik=[]
    znamenik=[]
    for i in reshenie.values():
        chiselnik.append(i.p)
        znamenik.append(i.q)

    print(chiselnik, znamenik)
    portibni_x=[]
    for i in range(len(chiselnik)):
        x=algoritm_evklida_with_a_b(znamenik[i], n, n)
        
        x=x*chiselnik[i]%(n-1)
        portibni_x.append(x)
    print(portibni_x)

    l, d=chetvertuykrok(alhpa, beta, s, n)
    print(l, d)
    log_alfa=poshuk_log(portibni_x,d, l, n )
    print(log_alfa)
    








index_calculus(10, int(17), int(47))