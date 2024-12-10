import random
print('''
_     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
                       _/ |                
                      |__/                 
''')
print("Welcome to Blackjack Game \n")
deck = [11,2,3,4,5,6,7,8,9,10,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,10]
player_hand = []
dealer_hand=[]
def add():
    num = random.choice(deck)
    player_hand.append(num)
    deck.remove(num)


def system_add():
    num2 = random.choice(deck)
    dealer_hand.append(num2)
    deck.remove(num2)

    
def dealer():
    
    system_add()
    dealer_total = sum(dealer_hand)
    while dealer_total<17:
        dealer_hand.append(random.choice(deck))
        dealer_total = sum(dealer_hand)
    print(f" Dealer hand = {dealer_hand}")
    if dealer_total >21:
        return "you win"
    return dealer_total


def player():
    system_add()
    print(f"Dealer hand = {dealer_hand}")
    add()
    choice ='y'
    player_total = sum(player_hand)
    while choice == 'y' and player_total<=21:
        add()
        print(f" Your hand = {player_hand}")
        if 11 in player_hand and player_total>21:
            player_hand.remove(11)
            player_hand.append(1)
            player_total=sum(player_hand)
        choice = input("Do you want to draw card ? 'Y' 'N' = ").lower()
        player_total = sum(player_hand)
        
    if choice == 'n':
        player_total=sum(player_hand)

    if player_total > 21:
        return "you lose"
    return player_total


def cal( player_total , dealer_total ):
    if player_total > dealer_total:
        print("you win")
    else:
        print("you lose")

you = player()
if you == 'you lose':
    print("you lose")
else:
    system = dealer()
    if system == 'you win':
        print("you win")
    else:
        cal(you,system)
    
