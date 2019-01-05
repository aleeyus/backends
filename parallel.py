from pprint import pprint
import multiprocessing
import collections
import time
import os

Scientist = collections.namedtuple('Scientist',[
	'name',
	'field',
	'born',
	'nobel'
	])

scientist = (
	Scientist(name="Aliyu Lawal", field="SE", born=1996, nobel=False),
	Scientist(name="Linus Tovel", field="CS", born=1956, nobel=True),
	Scientist(name="Bill Torelz", field="CS", born=1965, nobel=False),
	Scientist(name="Sachin Kafle", field="SE", born=1985, nobel=False),
	Scientist(name="Bucky Robert", field="CCNA", born=1985, nobel=True),
	Scientist(name="Vera Rubin", field="Astronomy", born=1928, nobel=False),
	Scientist(name="Ada Yonath", field="Chemistry", born=1939, nobel=True),
	Scientist(name="Marie Curie", field="Physics", born=1867, nobel=True)
	)

pprint(scientist)
print()

def transform(x):
	print(f'Process Id: {os.getpid()} working record {x.name}')
	time.sleep(1)
	result = {'name': x.name, 'age': 2017- x.born}
	print(f'Process Id: {os.getpid()} done record {x.name}')
	return result

if __name__ == '__main__':
	start = time.time()

	pool = multiprocessing.Pool(processes=8, maxtasksperchild=1)
	result = pool.map(transform, scientist)

	end = time.time()

	pprint(result)
	print(f"\n Time completed {end - start:.2f}s\n")