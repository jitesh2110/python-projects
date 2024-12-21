import tkinter
from tkinter import END
from tkinter import messagebox
import random
import pyperclip


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters =[random.choice(letters) for n in range(nr_letters)]
    password_symbols =[random.choice(symbols) for n in range(nr_symbols)]
    password_numbers =[random.choice(numbers) for n in range(nr_numbers)]
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password ="".join(password_list)
    passentry.insert(0,password)
    pyperclip.copy(password)

def adddata():
    username = userentry.get()
    webname = webentry.get()
    passdata = passentry.get()
    if len(username) ==0 or len(webname) == 0 or len(passdata) == 0:
        messagebox.showinfo(title='Missing', message="Please don't leave any field empty!")
    else:
        confirm = messagebox.askokcancel(title=webname, message=f"Details are as follow: \nEmail/Username: {username}"
                                                                f" \nWebsite: {webname} \nPassword: {passdata} \nPlease"
                                                                f" confirm it to save!")

        if confirm:
            with open("passward_data.txt", mode='a') as file:
                file.write(f"{webname} | {username} | {passdata}\n")
                userentry.delete(0, END)
                webentry.delete(0, END)
                passentry.delete(0, END)


window = tkinter.Tk()
window.config(pady=20,padx=20)

logo = tkinter.PhotoImage(file="logo.png")

canvas = tkinter.Canvas(width=200,height=190)
canvas.create_image(100,95,image =logo)
canvas.grid(column = 1, row = 0)

website = tkinter.Label(text='Website',font=('Roboto',12),highlightthickness=2)
website.grid(column = 0, row = 1,padx= 5, pady = 5)

username = tkinter.Label(text='Email/Username',font=('Roboto',12),highlightthickness=2)
username.grid(column = 0, row = 2,padx= 5, pady = 5)

password = tkinter.Label(text='Password',font=('Georgia',12),highlightthickness=2)
password.grid(column = 0, row = 3,padx= 5, pady = 5)

webentry = tkinter.Entry(highlightthickness=2)
webentry.focus()
webentry.grid(column = 1, row = 1,columnspan = 2,sticky = 'nsew',padx= 5, pady = 5)

userentry = tkinter.Entry(highlightthickness=2)
userentry.grid(column = 1, row = 2,columnspan = 2,sticky = 'nsew',padx= 5, pady = 5)

passentry = tkinter.Entry(highlightthickness=0)
passentry.grid(column = 1, row = 3,sticky = 'nsew',padx= 5, pady = 5)

genarate = tkinter.Button(text='Generate password', width=15,highlightthickness=2,bg='white',font=('Roboto',8,'bold')
                          ,command=generate_password)
genarate.grid(column = 2, row = 3,sticky = 'e',padx= 5, pady = 5)

add = tkinter.Button(text='add',width=40,highlightthickness=2,bg='white',font=('Roboto',8,'bold'),command=adddata)
add.grid(column = 1, row = 4,columnspan =2,sticky = 'nsew',padx= 5, pady = 5)

window.mainloop()
