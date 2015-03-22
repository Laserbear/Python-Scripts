#Christian Ng
import random

class Door(object):
	wins = 0
	losses = 0
	wins_Switch = 0
	losses_Switch = 0
	def __init__(self, type):
		self.type = type
	def Reveal(self):
		if self.type == 1:
			Door.wins = Door.wins + 1
		else:
			Door.losses = Door.losses + 1
	def Reveal_Switch(self):
		if self.type == 1:
			Door.wins_Switch = Door.wins_Switch + 1
		else:
			Door.losses_Switch = Door.losses_Switch + 1
door1 = Door(1)
door2 = Door(2)
door3 = Door(2)
trials = 1000000
for i in range(trials):
	choice = random.randint(1,3)
	if choice == 1:
		door1.Reveal()
	elif choice == 2:
		door2.Reveal()
	else:
		door3.Reveal()


	if choice == 1:
		door2.Reveal_Switch()
	elif choice == 2:
		door1.Reveal_Switch()
	elif choice == 3:
		door1.Reveal_Switch()
	
print "Trials: " + str(trials)
print "No switching wins: " + str(Door.wins)
print "No switching losses: " + str(Door.losses)
print "Switching wins: " + str(Door.wins_Switch)
print "Switching losses: " + str(Door.losses_Switch)


