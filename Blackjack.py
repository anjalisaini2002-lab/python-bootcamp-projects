import random
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
def deal():
    
    card=random.choice(cards)
    return card

user_cards=[]
comp_cards=[]


for i in range(2):
    new_card=deal()
    user_cards.append(new_card)



for i in range (2):
   comp_cards.append(deal())


user_sum=sum(user_cards)
comp_sum =sum(comp_cards)


def computer():
    global comp_sum
    
    while comp_sum<17 :
        comp_cards.append(deal())
        comp_sum = sum(comp_cards)
        print(f"comp cards: {comp_cards}, cuurent score: {comp_sum}")


print("go to day 11 see the solution make it perfect game.")
print("start playing ")
print(f"your cards: {user_cards}, current score: {user_sum}")
print(f"comp cards: {comp_cards[0]}")

repeat=input("type y to choose another card otherwise no to pass.")
if repeat=="y":
    user_cards.append (deal())
    user_sum = sum(user_cards)
    print(f"your cards: {user_cards}, current score: {user_sum}")
    print(f"comp cards: {comp_cards}, cuurent score: {comp_sum}")
    computer()
else:
    computer()


# ace logic for user
if user_sum > 21 and 11 in user_cards:
    user_sum -= 10

# ace logic for computer
if comp_sum > 21 and 11 in comp_cards:
    comp_sum -= 10


# ----- DECIDE WINNER -----

if user_sum > 21:
    print("You busted. Computer wins.")

elif comp_sum > 21:
    print("Computer busted. You win!")

elif user_sum > comp_sum:
    print("You win!")

elif user_sum < comp_sum:
    print("Computer wins.")

else:
    print("It's a draw.")





   
   

   










