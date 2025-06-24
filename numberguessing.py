import random 
max_attempts=5
secret_number=random.randint(1,10)
attempt=0
print("👾welcome to the random number guessing game..")
print("you have 5 attempts to guess what number i am thinking between 1 to 10!")

while attempt<max_attempts:
    guess=int(input(f"attempt {attempt + 1} guess the number: "))
    attempt+=1

    if guess < secret_number:
        print("oh oh too low go for another attempt!🎯")
    elif guess > secret_number :
        print("nope! too high this time! try again")
    else :
        print("correct!🙌🏻 you guessed the right number..")
        break







    











