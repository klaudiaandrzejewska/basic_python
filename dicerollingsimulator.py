# As the name of the program suggests, we will be imitating a rolling dice. This is one of the interesting python projects
# and will generate a random number each dice the program runs, and the users can use the dice repeatedly for as long as he wants.
# When the user rolls the dice, the program will generate a random number between 1 and 6 (as on a standard dice).
# The number will then be displayed to the user. It will also ask users if they would like to roll the dice again.
# The program should also include a function that can randomly grab a number within 1 to 6 and print it.
# This beginner-level python projects will help build a strong foundation for fundamental programming concepts.

import random
while True:
    roll_dice = input("Write start to dice roll: ")

    if roll_dice == "start":
        posiblle_results = [1, 2, 3, 4, 5, 6]
        result = random.choice(posiblle_results)
        print("Result of dice rolling is : " + str(result))

    while True:
        answer = str(input('Run again? yes/no: '))
        if answer in ('yes', 'no'):
            break
        print("invalid input.")
    if answer == 'yes':
        continue
    else:
        print("Goodbye")
        break



