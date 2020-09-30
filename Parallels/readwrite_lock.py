import threading
from readerwriterlock import rwlock

WEEKDAYS = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
today = 0
marker = rwlock.RWLockFair()

def calendar_reader(id):
	global today
	read_marker = marker.gen_rlock()
	name = 'Reader-' + str(id)
	while today < len(WEEKDAYS)-1:
		read_marker.acquire()
		print(f"{name} sees that today is {WEEKDAYS[today]} & read count: {read_marker.c_rw_lock.v_read_count}")
		read_marker.release()

def calendar_writer(id):
	global today
	write_marker = marker.gen_wlock()
	name = 'Writer-' + str(id)
	while today < len(WEEKDAYS)-1:
		write_marker.acquire()
		today = (today+1) % 7
		print(f"{name} update date to {WEEKDAYS[today]}")
		write_marker.release()

if __name__ == '__main__':
	for i in range(10):
		threading.Thread(target=calendar_reader, args=(i,)).start()

	for i in range(2):
		threading.Thread(target=calendar_writer, args=(i,)).start()