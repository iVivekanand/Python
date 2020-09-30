import threading
import os
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor

def perform_action(id):
	print(f"{os.getpid()} {threading.current_thread().getName()} performed action {id}")

if __name__ == "__main__":
	with ThreadPoolExecutor(max_workers=20) as pool:
		for action in range(200):
			pool.submit(perform_action, action)
	
	with ProcessPoolExecutor(max_workers=20) as pool:
		for action in range(200):
			pool.submit(perform_action, action)