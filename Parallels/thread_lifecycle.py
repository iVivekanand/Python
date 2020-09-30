import threading
import time

class UserThread(threading.Thread):
	def __init__(self):
		super().__init__()

	def run(self):
		print(f"User thread started and going to 3s wait state")
		time.sleep(3)
		print(f"User thread done waiting. Will terminate now")


if __name__ == '__main__':
	print(f"Main started and creating a user thread")
	user_thread = UserThread()
	print(f"	User thread alive? {user_thread.is_alive()}")

	print(f"Main requests user thread to (run) start")
	user_thread.start()
	print(f"	User thread alive? {user_thread.is_alive()}")

	print(f"Main sleeps in the interim")
	print(f"	User thread alive? {user_thread.is_alive()}")
	time.sleep(0.5)

	print(f"Main to wait for user thread to complete using join")
	user_thread.join()
	print(f"	User thread alive? {user_thread.is_alive()}")

	print(f"Main and user thread are finished")	