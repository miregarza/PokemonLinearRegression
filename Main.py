#w_in = x^(pseudoInv)*y
import numpy as np
import matplotlib.pyplot as plt
#import pandas as pd

file = open("pokemon.csv", "r")
print("***********************************")
node = []
for line in file:
	node.append(line.split(","))
	print(line)

def clean(readF):
	for i in readF:
		i[1] = i[1].replace("\r","")
		i[1] = i[1].replace("\n","")
	return(readF)

def linear(m,b):
	coord = []
	for i in range(221):
		x = (i*m)+ b
		coord.append(x)
	return(coord)
#use x = np.linalg.pinv(x)
#full = generatorX(10,0,100)
full = clean(node)
full.pop(0)
for i in range(len(full)):
	for j in range(len(full[i])):
		full[i][j]= int(full[i][j])
#hP and attack
x=[]
y=[]
print("THIS IS THE FULL: ", full)
for i in full:
	x.append([0,i[0]])
	y.append(i[1])
	plt.plot(i[0],i[1],marker='o', markersize=5, color="blue")
print("X is: ", x)
print("Y is: ", y)
w = np.dot(np.linalg.pinv(x),y)
print("Final w is", w[1])
plt.plot(linear(w[1],0), color = "red")


plt.xlabel("Pokemon HP")
plt.ylabel("Pokemon Attack Power")
plt.ylim(0,220)
plt.xlim(0,220)
plt.show()
