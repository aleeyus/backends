from model import threadx
from model import thready
import multiprocessing
import time
import sys
import os

#a = thready
#b = threadx

#p1 = multiprocessing.Process(target=threadx.function, args=10)
#p2 = multiprocessing.Process(target=thready.b, args=10)

#pool = multiprocessing.Pool(processes=3, maxtasksperchild=1)

#result = pool.map(a.function(10),b.function(10))

def calc_square(numbers):
	for n in numbers:
		time.sleep(1)
		print('Square ', str(n*n), 'Process Id',os.getpid())

def calc_cube(numbers):
	time.sleep(1)
	for n in numbers:
		print('Cube ', str(n*n*n), 'Process Id',os.getpid())

if __name__ == '__main__':
	arr = 2,3,8,9
	#pool = multiprocessing.Pool(processes=3, maxtasksperchild=1)
	p1 = multiprocessing.Process(target=calc_square, args=(arr,))
	p2 = multiprocessing.Process(target=calc_cube, args=(arr,))

	p1.start()
	p2.start()
	p1.join()
	p2.join()