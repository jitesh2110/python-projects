BACKGROUND_COLOR = "#B1DDC6"

import tkinter
import pandas
import random

data = pandas.read_csv('french_words.csv')
to_learn = data.to_dict(orient="records")
learned ={}
print(to_learn)
new_word = {}
def new_card():
    global new_word,timer
    window.after_cancel(timer)
    new_word = random.choice(to_learn)
    canva.itemconfig(title,text='French',fill='black')
    canva.itemconfig(word,text=new_word['French'],fill='black')
    canva.itemconfig(card_background,image=front_img)
    timer = window.after(3000, func=flip_card)

def flip_card():
    global new_word
    canva.itemconfig(card_background,image=back_img)
    canva.itemconfig(title,text='English',fill='white')
    canva.itemconfig(word,text=new_word['English'],fill='white')

def learned():
    to_learn.remove(new_word)
    new_card()

window = tkinter.Tk()
window.title("Flash card")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

timer = window.after(3000,func=flip_card)

canva = tkinter.Canvas(height=526, width=800)
front_img = tkinter.PhotoImage(file="card_front.png")
back_img = tkinter.PhotoImage(file='card_back.png')
card_background = canva.create_image(400,263, image=front_img)
canva.config(highlightthickness=0,bg= BACKGROUND_COLOR)
title = canva.create_text(400,150,text='Title',font=('Arial',40,'italic'))
word = canva.create_text(400,256,text='word',font=('Arial',60,'bold'))

canva.grid(row=0,column=0, columnspan=2)

wrong_img = tkinter.PhotoImage(file='wrong.png')
wrong = tkinter.Button(image =wrong_img, bg=BACKGROUND_COLOR, highlightthickness=0,command=new_card)
wrong.grid(column=0,row=1)

right_img = tkinter.PhotoImage(file='right.png')
right = tkinter.Button(image=right_img, bg=BACKGROUND_COLOR, highlightthickness=0,command=new_card)
right.grid(column=1,row=1)

window.after(3000,func=flip_card)

window.mainloop()
