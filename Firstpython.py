#Adding two numbers 
a = int(input(" Input number1: "))
b = int(input(" Input number2: "))
 
Add = a + b
 
print("Add:", Add)

#Multiplying two 3*3 matrices
import numpy as np

A= np.array([[1,2,3],[4,5,6],[7,8,9]])
B=np.array([[9,8,7],[6,5,4],[3,2,1]])
C=np.dot(A,B)
print('Matrix multiplication of A*B:',C)
