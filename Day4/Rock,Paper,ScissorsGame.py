print("Welcome to rock paper scissors game\n")
rock =("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper =("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

pick = [rock,paper,scissors]
choice = int(input("What is your choice ? 0 for rock 1 for paper 2 for scissors = "))
choice1 = random.randint(0,2)
if choice == choice1:
    print(f"{pick[choice]} \n it is draw")
elif choice1==1 and choice==0:
    print(f"you = {pick[choice]} \n system = {pick[choice1]} \n you lose")
    if choice1==2:
        print(f"you = {pick[choice]} \n system = {pick[choice1]} \n you win")
elif choice==1 and choice1==0:
    print(f"you = {pick[choice]} \n system = {pick[choice1]} \n you win")
    if choice1==2:
        print(f"you = {pick[choice]} \n system = {pick[choice1]} \n you lose")
elif choice==2 and choice1==0:
    print(f"you = {pick[choice]} \n system = {pick[choice1]} \n you lose")
    if choice1==1:
        print(f"you = {pick[choice]} \n system = {pick[choice1]} \n you win")

    
