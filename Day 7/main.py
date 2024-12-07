import ceaser_cipher_art

print(ceaser_cipher_art.logo)
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def crypt(message,shift,direction):
  encode = ""
  for i in message:
      if i in alpha:
          newposition = alpha.index(i)
          if direction == "encode":
              for i in range(0,shift):
                  newposition+=1
                  if newposition>alpha.index("z"):
                      newposition=alpha.index("a")
              encode +=alpha[newposition]        
          else:
              for i in range(0,shift):
                  newposition-=1
                  if newposition<alpha.index("a"):
                      newposition=alpha.index("z")
              encode +=alpha[newposition]

      else:
          encode+=i
  print(f"{direction.upper()}ED message is = {encode} ")        

work = True
while work:
  direction= input("Enter 'encode' to encrypt and 'decode' to decrypt = ")
  if direction=="encode" or direction=="decode":
      message = input("Enter the message = ").lower()
      shift = int(input("Enter the number of shift = "))
      crypt(message=message,shift=shift,direction=direction)
      select = input("Do you want to continue ? Y , N = ").lower()
      if select=="y":
          work=True
      else:
          work=False

  else:
      print("Please select correct choice")

