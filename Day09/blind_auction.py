from clear import clear
from art import logo
import math

print(logo)
bids = {}

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
       bid_amount = bidding_record[bidder]
       if bid_amount > highest_bid:
           highest_bid = bid_amount
           winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}") 
    

auction_going = True
while auction_going:
    name = input("What's your name? ")
    bid_price = int(input("What's your bid? $"))
    bids[name] = bid_price
    go = input("Are there any other bidders? Type 'yes or 'no'. \n").lower()
    if go == "yes":
        clear()
    elif go == "no":
        auction_going = False
        find_highest_bidder(bids)


