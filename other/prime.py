from math import sqrt

def prime(aNumber):
	'''return True if the number is prime, false otherwise'''
	if aNumber < 2: return False
	if aNumber == 2: return True
	if (( aNumber / 2 ) * 2 == aNumber) : 
		return False
	else:
		klist = int(sqrt(aNumber)+1)	
		for k in range(2,klist):
			if (( aNumber / k ) * k == aNumber ): return False
		return True

def fun(x):
	for i in range(x[0],x[1]+1):
		if prime(i):
			print i
	print 
    
count=int(raw_input())
t=[]
for num in range(count):   
	a_b=raw_input()
	a,b=a_b.split()
	t.append([int(a),int(b)])
for k in t:
	fun(k)

