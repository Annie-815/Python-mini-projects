import random
choices = ("r", "p", "s")
Emojis ={
    "r" :"🖤",
    "p" :"📃",
    "s" :"✂"
}

while True:
    user_choice = input("enter a choice between Rock paper or scissors (r/p/s): ").lower()
    if user_choice not in choices:
        print("Invalid Choice")
        continue
    computer_choice = random.choice(choices)
    print(f"You chose {Emojis[user_choice]}")
    print(f"Computer chose {Emojis[computer_choice]}")
    if user_choice == computer_choice:
        print("Tie")
    elif(
        (user_choice == "r" and computer_choice == 's') or
        (user_choice == "s" and computer_choice == "p")or
        (user_choice == "p" and computer_choice == "r")):
        print("Congratulations! you win")
    else:
        print("you loose")

    cont = input("Continue (y/n): ").lower()
    if cont == "n":
        break