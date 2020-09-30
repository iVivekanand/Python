from concurrent.futures import ThreadPoolExecutor
import time

def perform_action():
	print(f"Function performing action")
	time.sleep(3)
	return 43

if __name__ == "__main__":
	print(f"Main asking function to perform task and return result")
	with ThreadPoolExecutor() as pool:
		future = pool.submit(perform_action)
		print(f"Main can continue till result is available")
		print(f"Perform action function returned {future.result()}")