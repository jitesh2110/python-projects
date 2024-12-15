from question_model import Question
from data import question_data
from quiz_brain import brain
bank = []
for key in question_data:
    que = Question(key['text'],key['answer'])
    bank.append(que)

b= brain(bank)
while(b.status()):
    b.ask()
    print(f"Your score: {b.correct_answer}/{b.question_number}")
