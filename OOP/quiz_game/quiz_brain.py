class Quizbrain:
    
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        total_questions = len(self.question_list)
        if total_questions == self.question_number:
            return False
        else:
            return True
    
    def check_answer(self, current_answer, user_answer):
        if user_answer == current_answer.lower():
            print("You are Correct.")
            self.score += 1
        else:
            print("You are wrong")
        
        print(f"Your current score: {self.score}/{self.question_number}")
        print("\n")

    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        current_answer = current_question.answer
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ").lower()
        self.check_answer(current_answer,user_answer)
    
    
