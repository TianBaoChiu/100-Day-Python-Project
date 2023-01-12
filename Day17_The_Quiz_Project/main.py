from question_model import QuestionModel
from data import question_data
from quiz_brain import QuizBrain

question_list = []

for question in question_data:
    text = question['text']
    answer = question['answer']
    question_pair = QuestionModel(text, answer)
    question_list.append(question_pair)

quiz = QuizBrain(question_list)

while quiz.still_have_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
