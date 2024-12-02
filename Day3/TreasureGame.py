print(''' *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')

print("Welcome to the treasure island\n your mission is to find the treasure")
choice1 = input("you have two paths ahead choose Right path or Left path = ").lower()
if choice1 == "right":
    print("You fell into deep hole, GAME OVER \n")
elif choice1 == "left":
    choice2 = input("You see a lake infront of you will you swim or wait ? = ").lower()
    if choice2 =="swim":
        print("The lake was just an illusion you fell into darkness, GAME OVER")
    elif choice2 =="wait":
        print("very well , you preserved ")
        choice3 = input("you have a Red Yellow and Blue door infront of you which one will you open? ").lower()
        if choice3 == "blue":
            print("CONGRATULATIONS you finally found the treasure")
        else:
            print("You opend the door to HELL..., GAME OVER")

