import random

print("Welcome to jokenpô")
player = int(input("Type 0 for Rock, 1 for Paper, 2 for Scissors"))
machine = random.randint(0,2)

choice = ["--PEDRA--", "--PAPEL--", "--TESOURA--"]

print("You chose: ", choice[player])

print("Machine chose: ", choice[machine])

if machine == player:
    print("Draw")
else:
    match player:
        case 0:
            if machine == 2:
                print("You Win")
            else:
                print("You Lose")

        case 1:
            if machine == 0:
                print("You Win")
            else:
                print("You Lose")

        case 2:
            if machine == 1:
                print("You Win")
            else:
                print("You Lose")
