import random
from Help_utilities.Clear_screen import clear_screen


def Quiz_sem1():
    questions = [
        {"unit": "Unit 1 - Problem Solving & Algorithms","question": "What is the main idea of Top-Down Design?",
        "options": ["Breaking a large  problem into smaller problems",
                "Writing code without planning",
                "Using only loops",
                "Removing all functions"],"answer": 0,},
        
        {"unit": "Unit 1 - Problem Solving & Algorithms",
          "question": "Which of the following is commonly used to represent an algorithm graphically?",
        
            "options": [ "Dictionary",
                "Flowchart",
                "Tuple",
                "Variable"],"answer": 1,},
        
        {"unit": "Unit 1 - Problem Solving & Algorithms",
        
            "question": "What is the purpose of program verification?",
            "options": ["To check whether a program produces the expected results",
                "To make the program longer",
                "To remove variables",
                "To increase the number of comments"],"answer": 0,},
        
        
        {"unit": "Unit 1 - Problem Solving & Algorithms",
        
            "question": "Algorithm efficiency mainly studies:",
            "options": [
                "Program color",
                "Number of comments",
                "Resources and  operations required by an algorithm",
                "Variable names"],"answer": 2,},
        
        {"unit": "Unit 2 - Python Data, Expressions & Statements",
        
            "question": "Which of the following is an immutable Python data type?",
            "options": ["List", "Dictionary", "Tuple", "Set"],"answer": 2,},
        
        { "unit": "Unit 2 - Python Data, Expressions & Statements",
        
            "question": "What is the result of 2 + 3 * 4?",
            "options": ["20", "14", "24", "9"],
            "answer": 1, },
        
        {"unit": "Unit 2 - Python  Data, Expressions & Statements",
        
            "question": "In Python, which symbol is used to start a comment?",
            "options": ["//", "/*", "#", "--"],
            "answer": 2,},
        
        {"unit": "Unit 2 - Python Data, Expressions  & Statements",
        
            "question": "In a function definition, the variables that receive values are called:",
            "options": ["Arguments", "Parameters", "Operators", "Modules"],
            "answer": 1, },
        
        {"unit":  "Unit 3 - Fundamental Algorithms",
        
            "question": "What is the factorial of  5?",
            "options": ["25", "60", "120", "150"],
            "answer": 2,},
        
        { "unit": "Unit 3 - Fundamental Algorithms",
        
            "question": "What is the first number in the Fibonacci sequence commonly used in this syllabus?",
            "options": ["0", "1", "2", "-1"],
            "answer": 0, },
        
        {"unit": "Unit 3 - Fundamental Algorithms",
        
            "question": "Which statement skips the current iteration of a loop?",
            "options": ["break", "continue", "pass", "stop"],
            "answer": 1, },
        
        {"unit": "Unit 3 - Python Control Flow",
        
            "question": "Which statement is used when there are multiple conditions to check?",
            "options": ["if-elif-else", "for-only", " print", "import"],"answer": 0, },
        
        {"unit": "Unit 4 - Factoring Methods",
        
            "question": "What is the GCD of 24 and 36?",
            "options": ["6", "8", "12", "18"],
            "answer": 2,},
        
        {"unit": "Unit 4 - Factoring Methods",
        
            "question": "Which of the following is a prime number?",
            "options": ["21", "27", "29", "35"],
            "answer": 2,},
        
        {"unit": "Unit 4 - Factoring Methods",
        
            "question": "What are the prime factors of 60?",
            "options": ["2 x 2 x 3 x 5", "2 x 3 x 10", "4 x 15", "5 x 12"],
            "answer": 0,},
        
        {"unit": "Unit 4 - Factoring Methods",
            
            "question": "Which Python module can be used to generate pseudo-random numbers?",
            "options": ["random", "factor", "number", "prime"],"answer": 0,},
        
        {"unit": "Unit 5 - Array Techniques",
            
            "question": "Which operation changes [1, 2, 3] into [3, 2, 1]?",
            "options": ["Array reversal", "Array counting", "Partitioning", "Summation"], "answer": 0,},
        
        {"unit": "Unit 5 - Array Techniques",
           
            "question": "What is the maximum value in [5, 12, 3, 9]?",
            "options": ["3", "5", "9", "12"],
            "answer": 3, },
       
        {"unit": "Unit 5 - Python Lists",
            "question": "Which Python collection automatically stores only unique values?",
            "options": ["List", "Tuple", "Set", "String"],"answer": 2,},
        
        {"unit": "Unit 5 - Python Collections",
            "question": "Which Python data structure stores data using key-value pairs?",
           
            "options": ["List", "Tuple", "Set", "Dictionary"],
            "answer": 3,},
            {"unit": "Unit 5 - Array Techniques",
            
            "question": "If an ordered array is [2, 5, 7, 9], what is the 2nd smallest element?",
            "options": ["2", "5", "7", "9"],
            "answer": 1,},]

    quiz_questions = questions.copy()
    random.shuffle(quiz_questions)

    score = 0
    wrong_answers = []

    clear_screen() 
    print(" __________Semester1 Quiz_____________ ")
    print("       FIRST SEMESTER - VIT BHOPAL")
    clear_screen()
    print(f"\n{len(quiz_questions)} questions will be asked.")
    print("Each question carries 1 mark.")
    input("\nPress Enter to start.....")

    for number, question in enumerate(quiz_questions, start=1):
        user_answer = ask_question(question, number)

        if user_answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
            wrong_answers.append({"question": question["question"],
                    "your_answer": question["options"][user_answer],
                    "correct_answer": question["options"][question["answer"]],})

    percentage = (score / len(quiz_questions)) * 100

    clear_screen()
    print("                  QUIZ RESULT")
    clear_screen()

    print("Total questions :", len(quiz_questions))
    print("Correct answers :", score)
    print("Wrong answers   :", len(quiz_questions) - score)
    print("Percentage      :", round(percentage, 2), "%")

    if percentage >= 80:
        print("Performance :OUTSTANDING")
    elif percentage >= 60:
        print("Performance: V Good")
    elif percentage >= 40:
        print("Performance   : Work hard")
    else:
        print("Performance : better luck next time")

    if wrong_answers:
        clear_screen()
        print("              ANSWER REVIEW")
        clear_screen()

        for i, item in enumerate(wrong_answers, start=1):
            print("\n", i, ".", item["question"])
            print("Your answer    :", item["your_answer"])
            print("Correct answer :", item["correct_answer"])
    else:
        print("\nPerfect score! All answers are correct.")

    input("\nPress Enter to return to the main menu.....")


#DIsplay a question 

def ask_question(question, number):
    clear_screen()
    print("Question", number)
    print(question["unit"])
    clear_screen()
    print(question["question"])

    for i, option in enumerate(question["options"], start=1):
        print(f"{i}. {option}")

    while True:
        try:
            answer = int(input("Enter your answer (1-4): "))
            if 1 <= answer <= 4:
                return answer - 1
            print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Please enter a valid number.")


def main():
    while True:
        clear_screen()
        print("       PYTHONLAB - QUIZ & PRACTICE MODULE")
        print("=" * 60)
        print("1. Start Quiz")
        print("2. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            Quiz_sem1()
        elif choice == "2":
            print("\nThank you""\nHave a good day")
            break
        else:
            print("Wrong choice. Please try again.")


if __name__ == "__main__":
    main()
