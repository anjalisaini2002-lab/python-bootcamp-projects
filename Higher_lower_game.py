from game_data import game_data
import random

def check():
     if a["follower_count"] > b["follower_count"]:
        return "a"
     else:
        return "b" 


game_not_end=True
score=0
while game_not_end==True:
    a=random.choice(game_data)
    b=random.choice(game_data)
    while a == b:
        b = random.choice(game_data)
   
    correct=check() 
    print(f"Comapre A: {a['name']} a {a["description"]} from {a["country"]}")
    print("VS")
    print(f"Comapre B: {b['name']} a {b["description"]} from {b["country"]}")
    answer=input("which one has more followers? A OR B :").lower()
    if correct==answer:
        score+=1
        print(f"you are right. current score: {score}")
    else:
        print(f"you are wrong. current score is {score}. Game ended.")
        game_not_end=False
