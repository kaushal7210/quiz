class QuizBrain:

    def __init__(self, q_list):
        self.q_number = 0
        self.score = 0
        self.q_list = q_list

    def still_has_questions(self):
        return self.q_number < len(self.q_list)

    def next_question(self):
        current_question = self.q_list[self.q_number]
        self.q_number += 1
        user_ans = input(f"Q.{self.q_number}: {current_question.text}(True/False).")
        self.check_ans(user_ans, current_question.answer)

    def check_ans(self,user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            print("You got it right.")
            self.score += 1
            print(f"your current score is {self.score}/{self.q_number}.")
        else:
            print("That's wrong answer.")
            self.score += 0
            print(f"your current score is {self.score}/{self.q_number}.")
        print(f"The correct answer is {correct_ans}.""\n")
