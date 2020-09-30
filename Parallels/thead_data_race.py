import threading

gc1 = 0
gc2 = 0
loop_count = 1234
mutex = threading.RLock() # Re-entrant lock

def plus_gc1():
	global gc1
	mutex.acquire()
	gc1 += 1
	mutex.release()

def plus_gc2():
	global gc2
	mutex.acquire()
	gc2 += 1
	plus_gc1()
	mutex.release()

def incrementer():
	for i in range(loop_count):
		plus_gc1()
		plus_gc2()

if __name__ == '__main__':
	t1 = threading.Thread(target=incrementer)
	t2 = threading.Thread(target=incrementer)

	t1.start()
	t2.start()

	t1.join()
	t2.join()

	print(f"Global count 1: Expected {4*loop_count}, Actual {gc1}")
	print(f"Global count 2: Expected {2*loop_count}, Actual {gc2}")