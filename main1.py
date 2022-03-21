import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
file=open('D:\测试数据\\beibao9.in','r')
file1=open('D:\测试数据\\9.txt','w')
string=file.read().strip()
ss=string.split('\n')
s=[]
print(ss[2])
file1.write("\n".join(ss))
file.close()
file1.close()
a = []
b = []
c = []
m = 100
n = 300

def show(w, v):
    plt.figure(figsize=(5, 5), dpi=100)
    plt.xlabel('wight')
    plt.ylabel('value')
    plt.title('散点图')
    plt.scatter(w, v)
    plt.show()

def bag(n,c,w,v):
	res=[[-1 for j in range(c+1)] for i in range(n+1)]
	for j in range(c+1):
		res[0][j]=0
	for i in range(1,n+1):
		for j in range(1,c+1):
			res[i][j]=res[i-1][j]
			if j>=w[i-1] and res[i][j]<res[i-1][j-w[i-1]]+v[i-1]:
				res[i][j]=res[i-1][j-w[i-1]]+v[i-1]
	return res


fig,ax=plt.subplots()
ax1=plt.subplot(1,1,1)
for i in range(0,len(s)-1,2):
    x=list(map(int,s[i].split(',')))
    y=list(map(int,s[i+1].split(',')))
    ax1.scatter(x,y)
    plt.show()



def backtrack(i):
	global bestV,curW,curV,x,bestx
	if i>=n:
		if bestV<curV:
			bestV=curV
			bestx=x[:]
	else:
		if curW+w[i]<=c:
			x[i]=True
			curW+=w[i]
			curV+=v[i]
			backtrack(i+1)
			curW-=w[i]
			curV-=v[i]
		x[i]=False
		backtrack(i+1)



def GreedyAlgo(item, C, idex):
	'''贪心算法'''
	number = len(item)
	status = [0] * number
	total_weight = 0
	total_value = 0
	for i in range(number):
		if item[idex[i],0] <= C:
			total_weight += item[idex[i],0]
			total_value += item[idex[i],1]
			status[idex[i]] = 1
			C -= item[idex[i],0]
		else:
			continue
	return total_weight, total_value, status
