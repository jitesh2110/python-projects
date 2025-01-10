THEME_COLOR = "#375362"
import tkinter
from quiz_brain import QuizBrain
import time

class Gui:
    def __init__(self,quiz_brain: QuizBrain):
        self.points = 0
        self.quiz = quiz_brain
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(bg = THEME_COLOR,padx= 20,pady=20)
        self.score = tkinter.Label(text=f'score:{self.points}',bg=THEME_COLOR, fg='white',font=("Arial",10,'bold'))
        self.score.grid(row = 0,column = 1)

        self.canva = tkinter.Canvas(height=250,width=300)
        self.que = self.canva.create_text(150,125,text='question will be here',font=("Arial",20,'italic'),width=280)
        self.canva.grid(row =1,column =0, columnspan =2)

        self.t = tkinter.PhotoImage(file='images/true.png')
        self.rbutton = tkinter.Button(image=self.t,pady=20,padx=20,command=self.right)
        self.rbutton.grid(row=2,column =0,pady=20,padx=20)

        self.f = tkinter.PhotoImage(file='images/false.png')
        self.wbutton = tkinter.Button(image=self.f,pady=20,padx=20,command=self.wrong)
        self.wbutton.grid(row=2, column=1,pady=20,padx=20)

        self.getquestion()
        self.window.mainloop()

    def getquestion(self):
        self.canva.config(bg='white')
        self.canva.itemconfig(self.que,text =self.quiz.next_question())

    def right(self):
        result = self.quiz.check_answer('true')
        if result == 1:
            self.canva.config(bg = 'green')
            self.points = self.points+1
            self.score.config(text=f'score{self.points}')
            self.window.after(1000,func=self.getquestion)

        else:
            self.canva.config(bg='red')
            self.window.after(1000,func= self.getquestion)



    def wrong(self):
        result = self.quiz.check_answer('false')
        if result == 1:
            self.canva.config(bg='green')
            self.window.after(1000,func= self.getquestion)
        else:
            self.canva.config(bg='red')
            self.window.after(1000,func= self.getquestion)

