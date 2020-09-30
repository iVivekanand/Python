import threading

action_count = 1
mutex = threading.Lock()
barrier = threading.Barrier(10)

def cpu_work(work_units):
	x = 0
	for work in range(work_units * 1_000_000):
		x += 1

def second_action():
	global action_count
	cpu_work(1)
	barrier.wait()
	with mutex:
		action_count *= 2
		print(f"This is the second action. Count now is {action_count}")
	

def first_action():
	global action_count
	cpu_work(1)
	with mutex:
		action_count += 2
		print(f"This is the first action. Count now is {action_count}")
	barrier.wait()


if __name__ == "__main__":
	workers = []
	for i in range(5):
		workers.append(threading.Thread(target=first_action))
		workers.append(threading.Thread(target=second_action))
	for worker in workers:
		worker.start()
	for worker in workers:
		worker.join()
	print(f"Final action count is {action_count}")