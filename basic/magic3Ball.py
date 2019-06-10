import random

def getAnswer(answerNumber):
	if answerNumber == 1:
		return 'You win'
	elif answerNumber == 2:
		return 'Draw'
	else:
		return 'Lost'

r = random.randint(1,3)
fortune = getAnswer(r)
print(fortune)
