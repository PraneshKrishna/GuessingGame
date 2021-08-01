print ("Number Guessing Game")
import random
num = random.randrange(1,50)

guess = int(input("Guess a Number between 1 and 50: "))
while guess!= num:
      if guess<num:
          print("You need to guess higher than",)
          guess = int(input("Guess a Number between 1 and 50: "))
      else:
          print("Guess low")
          guess = int(input("Guess a Number between 1 and 50: "))

print("Nice! You actually did it!")          
            



