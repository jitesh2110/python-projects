import json
import requests
import tkinter


def click():
    response = requests.get(url='https://api.kanye.rest')
    response.raise_for_status()
    data = response.json()
    canva.itemconfig(message,text=data['quote'])



window = tkinter.Tk()
window.title('keny quote')
window.config(bg='white',pady=50,padx=50)

canva = tkinter.Canvas(width=300,height=414,bg='white',highlightthickness=0)
background = tkinter.PhotoImage(file='background.png')
canva.create_image(150,207,image=background)
message = canva.create_text(150,207,text='here will be quote',width=250,fill='white',font=('Arial',20,'bold'))
canva.pack()
keny = tkinter.PhotoImage(file='kanye.png')
button = tkinter.Button(image=keny,command=click,bg='white',highlightthickness=0)
button.pack()


window.mainloop()