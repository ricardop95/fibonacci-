#  aqui tienen 2 formas de ejecutar la secuencia de fibonacci
import random # random para obtener un numero alaetorio 
import math
from tkinter import N # para las operaciones matematicas 
# fb = fn-1 fn-2 

def fib (n):
    if n < 2:
        return n
    return fib(n-1) + fib (n-2)
for x in range (50):
    print (fib(x))
    
    
    
    # fibonacci 2
    num=int(input("ingrese la cantidad de serie que desea ver:\n"))
    primero=0
    segundo=1
    nuevo=0
    count=1
    if num ==1:
         print(0)
    if num ==2:
        print(0,1)
    if num ==3:
        print(0,1,1)
    if num == 4:
        print(0,1,1,2)
    else: 
        while (count<=num):
            print(nuevo)
            count+=1
            primero=segundo
            segundo=nuevo
            nuevo=primero+segundo