from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

def main():
    question_bank = [Question(question['question'], question['correct_answer']) for question in question_data]

    quiz = QuizBrain(question_bank)
    quiz_ui = QuizInterface(quiz)

    print("You've completed the quiz")
    print(f"Your final score was: {quiz.score}/{quiz.question_number}")

if __name__ == "__main__":
    main()
