import threading
import time

count = 0
mutex = threading.Lock()

def add():
	global count
	t_name = threading.current_thread().getName()
	local_count = 0
	print(f"Global count at start {count}")
	while count <= 20:
		if local_count and mutex.acquire(blocking=False):
			count += local_count
			print(f"{t_name} added {local_count} to {count}")
			local_count = 0
			time.sleep(0.3)
			mutex.release()
		else:
			time.sleep(0.1)
			local_count += 1
			print(f"{t_name}: {local_count} to add")

if __name__ == '__main__':
	t1 = threading.Thread(target=add, name='T1')
	t2 = threading.Thread(target=add, name='T2')

	start_time = time.perf_counter()

	t1.start()
	t2.start()

	t1.join()
	t2.join()

	print(f"Execution time: {time.perf_counter() - start_time: .2f}s")
	