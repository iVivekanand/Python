import threading

spoon = threading.Lock()
servings = 10
serving_taken = threading.Condition(lock=spoon) # Notification condition

def hungry(person_id):
	global servings

	while servings > 0:
		with spoon: # Context manager handles mutex acquire and release
			while (person_id == (servings % 5)) and (servings > 0):
				print(f"Not person {person_id}'s turn yet. Waiting for their turn.")
				serving_taken.wait()
			if servings > 0:
				servings -= 1
				print(f"Person {person_id} served! Servings left {servings}")
				serving_taken.notify_all()


if __name__ == "__main__":
	for person in range(5):
		threading.Thread(target=hungry, args=(person,)).start()
