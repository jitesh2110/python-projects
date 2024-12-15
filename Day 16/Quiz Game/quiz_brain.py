class brain:
    def __init__(self,q_list):
        self.question_number = 0
        self.question_list =q_list
        self.correct_answer = 0

    def ask(self):
        self.ans=input(f"Q.{self.question_number+1}: {self.question_list[self.question_number].text} ( True / False )? :").title()
        if self.ans == self.question_list[self.question_number].answer:
            print("You are right!")
            self.correct_answer+=1
        else:
            print("You are wrong!")
            print(f"Correct answer is {self.question_list[self.question_number].answer} ")
        self.question_number += 1

    def status(self):
        if self.question_number < 12:
            return True
        return False
