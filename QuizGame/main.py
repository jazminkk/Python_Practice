from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import random

question_bank = []
question_list = random.choices(question_data, k=5)

for data in question_list:
    question_text = data["question"]
    question_answer = data["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
print(question_bank[0].text)

quiz = QuizBrain(question_bank)

while quiz.has_next_question():
    quiz.next_question()

print("You're completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}.")

