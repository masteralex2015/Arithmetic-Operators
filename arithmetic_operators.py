# -*- coding: utf-8 -*-
"""Arithmetic Operators

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XFNvtp6y4fW1rFKoOshgDXuiijdQefMq
"""

a = int(input())
b = int(input())
x = a + b 
y = a - b 
z = a * b
print(x)
print(y)
print(z)
---------------------------------------------------------------------
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    if a >= 1 and a <= 10**10 and b >= 1 and b <= 10**10:5
      print(a + b)
      print(a - b)
      print(a * b)
    else:
      print ("invalid number ")
--------------------------------------------------------------------
minValue = 10
maxValue = 50

s = input("input your number ")
try:
  n = int(s)
  print(s)
  if (minValue > n or maxValue < n):
    print("invalid number")
  else:
    print("valid number")

except:
    print("call the coder")
---------------------------------------------------------------------
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)
