from data import question_data
from question_model import Question
from quiz_brain import Quizbrain

question_bank = []

for item in question_data:
    question = Question(item["text"], item["answer"])
    question_bank.append(question)

quiz = Quizbrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz!")
print(f"Your final score: {quiz.score}/{quiz.question_number}")