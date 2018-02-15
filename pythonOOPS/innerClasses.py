
class Human:

	def __init__(self):
		self.name ='PyBot'
		self.head = self.Head()
		self.brain = self.Brain()

	class Head:
		def talk(self):
			return "Talking ..."

	class Brain:
		def think(self):
			return "Thinking ..."



if __name__ == '__main__':
	pybot = Human()

	print pybot.name
	print pybot.head.talk()
	print pybot.brain.think()