import threading
import time

def garbage_collector():
	garbage_count = 0
	while True:
		print(f"Garbage {garbage_count} collected")
		garbage_count += 1
		time.sleep(1)

if __name__ == '__main__':
	gc_thread = threading.Thread(target=garbage_collector)
	gc_thread.daemon = True
	gc_thread.start()

	print(f"Main is running")
	time.sleep(0.5)

	print(f"Main is running")
	time.sleep(0.5)

	print(f"Main is running")
	time.sleep(0.5)

	print(f"Main is done")