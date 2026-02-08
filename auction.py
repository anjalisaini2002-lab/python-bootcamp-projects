print("Welcome to Secret Auction Program")

auction={}
auction_start=True
while auction_start:
  name=input(f'What is your name:')
  bid=input("Enter your bid: Rs.")

  auction[name]=bid
  print(auction)
      
  restart=input("Are there any other bidders? YES or NO").lower()
  if restart=="no":
    auction_start=False
    print("Auction ended.")


highest_key= max(auction,key= auction.get)


print(f"Winner is {highest_key} and highest bid is {auction[highest_key]}")


