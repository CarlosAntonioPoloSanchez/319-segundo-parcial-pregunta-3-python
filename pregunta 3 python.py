# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def superfibo(op):
    def fibonacci(b):
        if b<2:
            return b
        else:
            return (fibonacci(b-1)+fibonacci(b-2))
    def bucle(a,b):
        for i in range(a):
            if i==(a-1):
                b=b+str(fibonacci(i))
            else:
                b=b+str(fibonacci(i))+", "
        return b
    
    if op == "bucle":
         return bucle
    elif op == "fibonacci":
         return fibonacci
    
print ("insertar un numero")
a=int(input())
b=""
x=superfibo("bucle")
print(x(a,b))
