import random
import data
import os
import art

def pick():
    a = data.data.index(random.choice(data.data))
    return a

def compare( dataA , dataB ):
    if data.data[dataA]['follower_count'] > data.data[dataB]['follower_count']:
        return dataA
    elif data.data[dataA]['follower_count']< data.data[dataB]['follower_count']:
        return dataB
    else:
        return 

def take(dataA,dataB):
    print(art.logo)
    print(f"Compare A:{data.data[dataA]['name']}\n is a {data.data[dataA]['description']}\n {data.data[dataA]['country']} ")
    print(art.vs)
    print(f"Against B: {data.data[dataB]['name']}\n is a {data.data[dataB]['description']}\n {data.data[dataB]['country']} \n")
    print(f"Your score is : {score}")
    answer = input("Who has more followers ? Select 'A'  'B' = \n").lower()
    if answer == 'a':
        return dataA
    else:
        return dataB

def check( system , user ):
    global score
    if system == user:
        score+=1
        return True
    else:
        print(f"You are wrong! , Your Score is  = {score}")
        return False

def game():
    dataA = pick()
    chain = True
    while chain:
        dataB = pick()
        system_answer = compare( dataA , dataB )
        user_answer = take( dataA , dataB )
        result = check( system = system_answer , user = user_answer )
        if result == True:
            dataA =dataB
            os.system('clear')
        else:
            chain = False

new_game = True
while new_game:
    score = 0
    game()
    new = input("D you want to play new game ? 'Y' 'N' = ").lower()
    if new == 'y':
        new_game = True
        os.system('clear')
    else:
        new_game = False
