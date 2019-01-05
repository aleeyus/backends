import time

def isPrime(n):
	if n == 1:
		return False
	for d in range(2,n):
		if n%d == 0:
			return False
	return True
t1 = time.time()
for n in range(1,1000000):
	n, isPrime(n)
t2 = time.time()
print("Time completed", t2-t1)
