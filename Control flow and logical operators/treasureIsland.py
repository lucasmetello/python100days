print("Welcome to the Treasure Island. Your mission is to find the Treasure.\n")
choice = input("You are at a cross road, where do you want to go? 'left' or 'right'\n")

if choice == "right":
    print("Game Over")
else:

    print("You come to a lake. There is a island in the lake.\n")
    choice = input("'Wait' to a boat or try 'swim' across\n")

    if choice == "swim":
        print("Game Over")
    else:

        print("You arrive at the island unharmed. There is a house with 3 doors\n")
        choice = input("One 'red', one 'yellow' and one 'blue'. Witch colour do you choice?\n")

        if choice == "red" or choice == "blue":
            print("Game Over")
        else:
            print("You Win")
