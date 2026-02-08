print("""  _   _                 _                  _____                     _                _____                      
 | \ | |               | |                / ____|                   (_)              / ____|                     
 |  \| |_   _ _ __ ___ | |__   ___ _ __  | |  __ _   _  ___  ___ ___ _ _ __   __ _  | |  __  __ _ _ __ ___   ___ 
 | . ` | | | | '_ ` _ \| '_ \ / _ \ '__| | | |_ | | | |/ _ \/ __/ __| | '_ \ / _` | | | |_ |/ _` | '_ ` _ \ / _ \
 | |\  | |_| | | | | | | |_) |  __/ |    | |__| | |_| |  __/\__ \__ \ | | | | (_| | | |__| | (_| | | | | | |  __/
 |_| \_|\__,_|_| |_| |_|_.__/ \___|_|     \_____|\__,_|\___||___/___/_|_| |_|\__, |  \_____|\__,_|_| |_| |_|\___|
                                                                              __/ |                              
                                                                             |___/                               """)


#patorjk.com for ascii art


print("Welcome to the Number guessing game.")
print("I'm thinking a number between 0 to 50. Guess it.")
#import random number for guessing it.
import random
num=random.randint(1,50)


#choose diffculty level
difficulty_level=input("Choose the difficulty level. easy or hard:")

#easy level
def easy():
    easy_attempt=10
    while easy_attempt>0:
        print(f"you have {easy_attempt} guesses left.")
        guess=int(input("Make a guess:"))
        if num>guess:
            print("Too low.Guess again.")
            easy_attempt-=1 
           
        elif num<guess:
            print("Too high.Guess again")
            easy_attempt-=1
            
        elif num==guess:
            print("you win")  
            return   # stop function immediately 
    
    print("you lose.") 
    

#hard level        
def hard():
    hard_attempt=5
    while hard_attempt>0:
        print(f"you have {hard_attempt} guesses left.")
        guess=int(input("Make a guess:"))
        if num>guess:
            print("Too low.Guess again.")
            hard_attempt-=1
            
        elif num<guess:
            print("Too high.Guess again")
            hard_attempt-=1
        elif num==guess:
            print("you win")
            return   # stop function immediately
    print("you lose")
    


# select level difficulty
if difficulty_level=="easy":
    easy()
else:
    hard()





