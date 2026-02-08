
import random

print("who will pay the bill. Take a guess in PYTHON...")

friends=["anjali","rv","jannat","priya","Angela"]


#option 1
random_index=random.randint(0,5)
if (random_index==1):
    print("anjali will pay.")
elif(random_index==2):
    print("Rv will pay.")
elif(random_index==3):
    print("jannat will pay.")
elif(random_index==4):
    print("priya will pay.")
elif(random_index==5):
    print("angela will pay.")
else:
    print("guess again.")

#option 3
print(friends[random_index])

#option 2
print(random.choices(friends))

