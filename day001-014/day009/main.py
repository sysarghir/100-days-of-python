# The Secret Auction 

import art as art
import os as os
from time import sleep

auction_bids = {}


def add_bids():
    print(art.logo)

    more_bidders = "yes"
    winner_name = ""
    winner_value = 0

    while more_bidders != "no":
        bid_name = input("What is your name?: ")
        bid_value = int(input("What's your bid?: $"))

        auction_bids[bid_name] = bid_value

        more_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ")
        
        if more_bidders != "no" :
            os.system("cls")
        else:
            os.system("cls")
            for name in auction_bids:
                if auction_bids[name] > winner_value:
                    winner_name = name
                    winner_value = auction_bids[name]
            print(f"The winner is {winner_name} with a bid of ${winner_value}")


os.system("cls")
add_bids()

