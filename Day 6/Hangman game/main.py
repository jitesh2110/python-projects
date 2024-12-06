import random
import hangman_art
import hangmanwords

print(hangman_art.logo)
print("Welcome to Hangman Game \n")

word = random.choice(hangmanwords.words)
length = len(word)
sword = "_"*length
swordlist = list(sword)
print(swordlist)
loop = length
life = 0

while loop>0 and life<6: 
    check = input("Guess the latter = ").lower()
    if check in swordlist:
        print("You have already guessed this letter")
    for i in range(0,length):
        if word[i]==check and swordlist[i] == "_":
            print("You have guessed the latter correctly ")
            swordlist[i]=check
            loop-=1
        
    if check not in word:
            print("You have guessed the latter incorrectly")
            print(f"{hangman_art.stages[life]}")
            life+=1

    print(swordlist)

if life == 6:
    print("You Lose ")
else:
    print("You Win ")
