import random
import threading
import time

charger = threading.Semaphore(10)

def cellphone():
	name = threading.current_thread().getName()
	with charger:
		print(f"{name} is charging")
		time.sleep(random.uniform(1, 2))
		print(f"{name} finished charging")

if __name__ == "__main__":
	for phone in range(10):
		threading.Thread(target=cellphone, name=f"Phone-{phone}").start()