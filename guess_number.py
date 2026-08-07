import random

secret_number= random.randint(1,100)

#maximum no. of attempts
max_attempts=6

print("Welcome to Guess the number Game: ")
print("Select the no. between 1 and 100 ")
print(f"You have maximum {max_attempts} to guess the correct no: \n")

#Use the loop to Guess no:

for attempt in range(1, max_attempts+1):
    guess=int(input(f"Enter your {attempt}: Enter your guess: "))
    #This If-else stats help make game little bit simple
    if guess==secret_number:
        print(f"Congratulations you guessed the correct Number ({secret_number}) in {attempt} attempt(s).")
    elif guess < secret_number:
        print("Your number is small! Try again.\n")
    else:
     print("Its too high")
     
else:
    print(f"\n Game Over! You give your all attempts.")
    print(f"The correct no. was {secret_number}")
        