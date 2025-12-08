class Observer:
	def update(self, message):
		print(f"Received update: {message}")

class Subject:
	def __init__(self):
		self.observers = []
	
	def attach(self, observer):
		self.observers.append(observer)
	
	def notify(self, message):
		for observer in self.observers:
			observer.update(message)

# Test
subject = Subject()
obs1, obs2 = Observer(), Observer()
subject.attach(obs1)
subject.attach(obs2)
subject.notify("Update available!")