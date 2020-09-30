import multiprocessing as mp
import time

serving_line = mp.Queue(5)
consumer_count = 5

def cpu_work(work_units):
	x = 0
	for work in range(work_units * 1_000_000):
		x += 1

def producer(serving_line):
	for i in range(200):
		serving_line.put_nowait("Item #"+str(i))
		print(f"Served item {i}, - remaining capacity: {serving_line._maxsize-serving_line.qsize()}")
		time.sleep(0.2)
	for i in range(consumer_count):
		serving_line.put_nowait("This is the end")
	
def consumer(serving_line):
	while True:
		item = serving_line.get()
		if item == "This is the end":
			break
		print(f"Consumed item {item}")
		cpu_work(4)


if __name__ == "__main__":
	for i in range(consumer_count):
		mp.Process(target=consumer, args=(serving_line,)).start()
	mp.Process(target=producer, args=(serving_line,)).start()