import os
import threading
import multiprocessing as mp

def cpu_waster():
	while True:
		pass

if __name__ == '__main__':
	print(f"\nProcess ID: {os.getpid()}")
	print(f"Thread Count: {threading.active_count()}")
	
	for thread in threading.enumerate():
		print(thread)
	
	print(f"\nStarting 2 CPU wasters")
	for i in range(2):
		mp.Process(target=cpu_waster).start()
	
	print(f"\nProcess ID: {os.getpid()}")
	print(f"Thread Count: {threading.active_count()}")
	
	for thread in threading.enumerate():
		print(thread)
