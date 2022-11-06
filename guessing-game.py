# creating variables before game starts
import random
import time

intro1 = "Welcome to my dungeon. To escape, you'll have to guess the number correctly."
intro2 = "If you don't, you stay here with me FOREVER!"
# game starts here
# added time.sleep() for visual effects
print(intro1)
time.sleep(2)
print(intro2)
time.sleep(2)
n = random.randint(1, 100)

run = True
while run:
    playerchoice = int(input('Your choice:'))
# checking to see if the number guessed by the player is higher, lower, or correct
    if playerchoice == n:
        print('Rats, you guessed the number correctly. I guess I have to let you go now')
        run = False
    elif playerchoice > n:
        print('Your guess was higher than my number. Try again.')
    elif playerchoice < n:
        print('Your guess was lower than my number. Try again.')
    else:
        print('Error. Restart program.')
