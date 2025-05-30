import random
number = 0
while True:
    choice = input(f"roll the dice? (y/n): ").lower()
    if choice == 'y':
        randomnumber1 = random.randint(1,6)
        randomnumber2 = random.randint(1,6)
        print(f"({randomnumber1}, {randomnumber2})")
    elif choice == 'n':
        print("Thanks for playing")
        break
    else:
        print("Invalid choice please choose between y or n")