import sys,os
from  numpy import *

def load_data():
	V = []
	for line in sys.stdin:
		line_list = line.split(' ')
		V.append([float(a) for a in line_list])
	return mat(V)

def err(W,H,V,e,m,n):
	V_new = W * H
	E = V - V_new
	err = 0 
	for i in range(m):
		for j in range(n):
			err += E[i,j] * E[i,j]
	print err
	if err <e :
		return True
	return False

def nmf(V,r,k,e):
	m, n = shape(V)
	W = mat(random.random((m, r)))
	H = mat(random.random((r, n)))
	for it in range(k):
		print it
		if err(W,H,V,e,m,n):
			break
		middle_a = W * H * H.T
		middle_b = V *H.T
		for i in range(m):
			for j in range(r):
				if middle_a[i,j] !=0:
					W[i,j] = W[i,j] *middle_b[i,j]/middle_a[i,j]

		middle_a = W.T * W *H
		middle_b = W.T * V
		for i in range(r):
			for j in range(n):
				if middle_a[i,j] !=0:
					H[i,j] = H[i,j] * middle_b[i,j] / middle_a[i,j]
	return W,H

V = load_data()
W,H  = nmf(V,3,100,1e-3)

print "V:" ,V
print "W:" ,W
print "H:" ,H
print "W*H:" ,W *H

