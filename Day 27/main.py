import tkinter

window = tkinter.Tk()
window.minsize(300,200)
window.title("Miles to Km calculator")

lableM =tkinter.Label(text='Miles',font=("Verdana", 16, "bold italic"))
lableM.grid(column = 2,row =0, padx = 5,pady = 5)

lableK =tkinter.Label(text='Km',font=("Verdana", 16, "bold italic"))
lableK.grid(column = 2,row =1, padx = 5,pady = 5)

lableI =tkinter.Label(text='Is Equal To:',font=("Verdana", 12, "bold italic"))
lableI.grid(column = 0,row =1, padx = 5,pady = 5)

lableA = tkinter.Label(text='0',font=("Verdana", 16, "bold italic"))
lableA.grid(column = 1,row = 1, padx = 5,pady = 5)
def click():
    miles = int(entry.get())
    km = round(miles * 1.60934,2)
    lableA.config(text=f"{km}")

button = tkinter.Button(text="Calculate",command=click,)
button.grid(column =1,row = 2 ,padx = 5,pady = 5)

entry = tkinter.Entry()
entry.grid(column =1,row =0,padx = 5,pady = 5)


window.mainloop()
