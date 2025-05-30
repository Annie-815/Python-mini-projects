import random
randomnumber = random.randint(1,100)
while True:
    try:
        guess = int(input("Enter a number between 1 and 100: "))
        if guess > randomnumber:
            print("the number is too high")
        elif guess < randomnumber:
            print("The number is too low")
        else:
            print("Congratulations you guessed the number")
            break

    except ValueError:
        print("invalid choice: Enter a numerical value")