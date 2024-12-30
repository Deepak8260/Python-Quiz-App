import json

class QuizApp:
    def __init__(self, questions_file):
        self.questions_file = questions_file
        self.questions = self.load_questions()
        self.score = 0

    def load_questions(self):
        """Load questions from a JSON file."""
        try:
            with open(self.questions_file, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            print("Error loading questions. Please check the file.")
            return []

    def ask_question(self, question):
        """Ask a single question."""
        print(f"\n{question['question']}")
        for i, option in enumerate(question['options'], 1):
            print(f"{i}. {option}")

        choice = int(input("Your choice (1/2/3/4): "))
        return question['options'][choice - 1] == question['answer']

    def start_quiz(self):
        """Start the quiz."""
        if not self.questions:
            print("No questions available.")
            return

        print("\nWelcome to the Quiz!")
        for question in self.questions:
            if self.ask_question(question):
                print("Correct! 🎉")
                self.score += 1
            else:
                print(f"Wrong! The correct answer was: {question['answer']}")

        print(f"\nQuiz over! Your score: {self.score}/{len(self.questions)}")

if __name__ == "__main__":
    quiz = QuizApp("x.json")
    quiz.start_quiz()
