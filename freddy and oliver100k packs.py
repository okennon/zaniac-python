import random
number=random.randrange(0, 100)

guess=-1
while guess != number:
	guess = raw_input("Guess a number between 0 and 100: ")
	guess=int(guess)

	if guess<number:
		print("Too low!")
	elif guess>number:
		print("Too high")


print("you win!")
