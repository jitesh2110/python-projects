import os
import art

print(art.logo)
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

bids = {}

def add_bids(name,bid):
    bids[name]=bid

def calc():
    winner = ""
    highest = 0
    for key in bids:
        if bids[key]>highest:
            highest=bids[key]
            winner = key
    print(f"The winner is {winner} with bid = ${bids[winner]}")

print("Welcome to silent auction program \n ")
state = "yes"
while state == "yes":
    name = input("What is your name? = ")
    bid = int(input("What is your bid? = $"))
    add_bids(name,bid)
    state = input("Are there any other bidders? 'yes'  'no' = ").lower()
    if state == "yes":
        clear()
    elif state == "no":
        calc()
