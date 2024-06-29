import random
import time

def display_intro():
    intro_text = """
You are in a land full of dragons. In front of you, you see two caves. In one cave, 
the dragon is friendly and will share his treasure with you. 
The other dragon is greedy and hungry, and will eat you on sight.
"""
    print(intro_text)

def choose_cave():
    cave = ""
    while cave != "1" and cave != "2":
        print("wich cave will you go into? (1 or 2)")
        cave = input()
    return cave

def bright_object():    
    print("In the dark you can see a bright object. Do you risk taking it?. press 1 to take the object")
    bright_object = input()
    return bright_object

def check_cave(chosen_cave):
    print("You approach the cave...")
    time.sleep(2)
    print("It is dark and spooky...")
    time.sleep(2)
    print("A large dragon jumps out in front of you! He opens his jaws and ...")
    print()
    time.sleep(2)
    friendly_cave = random.randint(1,2)
    if chosen_cave == str(friendly_cave):
        print('Gives you his treasure!')
    else:
        sword = random.randint(1,2)
        if str(sword) == bright_object():
            print("You find a sword with which you cut the dragon in half.")
        else:
            print("bad luck hero, the shiny object was spoon. Gobbles you down in one bite!")





play_again = "yes"
while play_again == "yes" or play_again == "y":
    display_intro()
    cave_number = choose_cave()
    check_cave(cave_number)


    print("Do you want to play again? (yes or no)")
    play_again = input()