#guess the letter game

import random

word_list=["camel","baboon","anjali"]

guessed_letter=random.choice(word_list)

print(guessed_letter)
length=len(guessed_letter)

placeholder=""
for pos in range(length):
    placeholder+="_"
print(placeholder)

live=5

gameover=False
correct_letters=[]
while not gameover:
    user=input("Enter your guessed letter: ").lower()
    if user in correct_letters:
        print(f"you already guessed this letter {user}")
    display=""

    for char in guessed_letter:
        if char==user:
            display+=char
            correct_letters.append(user)
        elif char in correct_letters:
            display+=char
        else:
            display+="_"

    print(display)
    if "_" not in display:
        print("you win")
        gameover=True
    if user not in guessed_letter:
        live-=1
        print(f"you have {live} lives left.")
        print(f"you guessed wrong letter {user}.you lose a life")
        if live==0:
            gameover=True
            print("you lose")