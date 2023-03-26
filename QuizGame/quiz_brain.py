class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        guess = input(f"Q.{self.question_number}: {current_question.text} (True/False)?").lower()
        self.check_answer(guess, current_question.answer.lower())

    def has_next_question(self):
        total_questions = len(self.question_list)
        return self.question_number < total_questions

    def check_answer(self, user_guess, correct_answer):
        if user_guess == correct_answer:
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The answer is {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}.\n")

