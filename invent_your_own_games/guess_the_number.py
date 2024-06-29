import random
guesses_taken = 0

print("Hello! what is your name?")

my_name = input()

number = random.randint(1,20)
print('Well, ' + my_name + ', I am thinking of a number between 1 and 20.')

for guesses_taken in range(6):
    print('Taken a guess.')
    guess = input()
    guess = int(guess)

    if guess > 20:
        print(f'No sea guevon {my_name}, el nro es muy alto')
        break
    elif guess < 1:
        print(f'No sea pendejo {my_name}, el nro es muy bajo')
        break

    if guess < number:
        print("Your guess is too low. ")
    if guess > number:
        print("Your guess is too high. ")
    if guess == number:
        break

if guess == number:
    guesses_taken = str(guesses_taken + 1)
    print("Good job, " + my_name + "! You guessed my number in " + guesses_taken + " guesses!")

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number + '.')