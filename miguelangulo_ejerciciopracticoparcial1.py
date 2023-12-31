# -*- coding: utf-8 -*-
"""MiguelAngulo_EjercicioPracticoParcial1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HFy6nFvVQqPwU_YGA9QMvMJJChyKVR8d
"""

#Miguel Angel Angulo - 2170812
def Collatz(n):
  if( n <= 258):
    print("\nSecuencia de Collatz para n =",n)
    print(n)
    while (n != 1):
      if(n % 2 == 0):
        n = int(n / 2)
        print(n)
      elif(n % 2 != 0):
        n = 3*n + 1
        print(n)
  else:
    print("el número ingresado es mayor a 258, por favor vuelva a ingresar los datos.")

#Ultimo digito codigo: 2, por lo tanto N = 5
suma = 0
for i in range(5):
  i = int(input("Ingrese un número natural:\n"))
  suma = suma + i
N = int(suma / 5)

#Ejecutamos la conjetura de Collatz para el N resultante:
Collatz(N)