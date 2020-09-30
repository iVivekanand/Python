import os
import threading

def cpu_waster():
	while True:
		pass

print(f"\nProcess ID: {os.getpid()}")
print(f"Thread Count: {threading.active_count()}")

for thread in threading.enumerate():
	print(thread)

print(f"\nStarting 2 CPU wasters")
for i in range(2):
	threading.Thread(target=cpu_waster).start()

print(f"\nProcess ID: {os.getpid()}")
print(f"Thread Count: {threading.active_count()}")

for thread in threading.enumerate():
	print(thread)
