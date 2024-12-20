import tkinter
import math

reps = 0
mark = ''

def countdown(count):
    global reps
    global mark
    if reps != 0:
        min = math.floor(count / 60)
        sec = count % 60
        if sec <10:
            sec = f"0{sec}"
        canva.itemconfig(canva_text,text =f"{min}:{sec}")
        if count > 0:
            window.after(1000,countdown,count -1)
        else:
            if reps %2 == 0 or reps == 7:
                mark = mark+'✔'
            lablemark.config(text=mark, bg='#FFC0CB', fg='#32CD32', font=('Georgia', 10))
            timer()
    else:
        canva.itemconfig(canva_text, text=f"00:00")


def timer():
    global reps
    reps +=1
    if reps %2 != 0 and reps <8:
        value = 25
        lablehead.config(text="Work",bg='#FFC0CB',fg='#32CD32',font=('Georgia',25,'bold'))
    elif reps %2 == 0 and reps <8:
        value = 5
        lablehead.config(text="Short Break", bg='#FFC0CB', fg='#32CD32', font=('Georgia', 25, 'bold'))
    else:
        value = 30
        lablehead.config(text="Long Break", bg='#FFC0CB', fg='#32CD32', font=('Georgia', 25, 'bold'))

    countdown(value)

def restart():
    global reps
    global mark
    reps = 0
    mark = ''

window = tkinter.Tk()
window.title("Pomodoro")
window.config(bg= '#FFC0CB',padx=100,pady=100)

image = tkinter.PhotoImage(file='tomato.png')
canva = tkinter.Canvas(width=200 , height=223,bg = '#FFC0CB',highlightthickness=0)
canva.create_image(100,110,image=image)
canva_text =canva.create_text(100,122,fill='white',text='00:00',font=("Roboto Mono", 28, "bold"))
canva.grid(column =1,row=1)


lablehead= tkinter.Label(text="Timer",bg='#FFC0CB',fg='#32CD32',font=('Georgia',25,'bold'))
lablehead.grid(column=1,row=0)

lablemark = tkinter.Label(bg='#FFC0CB',fg='#32CD32',font=('Georgia',10))
lablemark.grid(column= 1,row =3)

buttonS = tkinter.Button(text='Start',bg ='#FFC0CB',fg ='black',font=('Georgia',8,'bold'),command=timer)
buttonS.grid(column=0,row=2)

buttonR = tkinter.Button(text='Reset',bg='#FFC0CB',fg='black',font=('Georgia',8,'bold'),command=restart)
buttonR.grid(column = 2,row=2)

window.mainloop()
