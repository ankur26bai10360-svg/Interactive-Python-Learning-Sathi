# Interactive Python Learning Sathi

A beginner-friendly Python learning project for first-semester students. It combines unit-wise study notes with a quiz system in one console application, so learners can revise concepts and test themselves without switching between multiple resources.

## About the Project

This project was created to make Python revision easier for students who are new to programming. Instead of searching through separate notes and question banks, they can open one menu, choose a unit, study the concepts, and then take a quiz to check their understanding.

The application is built as a simple terminal-based program and is designed for educational use.

## Features

- Menu-based navigation for all Python units
- Separate study section for each unit
- Quiz mode with score summary and answer review
- Beginner-friendly console interface
- Modular code structure for easy understanding and future expansion

## Units Covered

- Unit 1: Introduction to Problem Solving and Algorithms
- Unit 2: Python Data, Expressions and Statements
- Unit 3: Control Flow, Loops and Fundamental Algorithms
- Unit 4: Factoring Methods, GCD and Prime Numbers
- Unit 5: Arrays and List Processing Techniques

## Technologies Used

- Python 3
- Python built-in `unittest` module for testing
- VS Code for development
- Git and GitHub for version control

## Project Structure

```text
Project/
├── main.py
├── README.md
├── statement.md
├── Data/
│   └── Quiz.py
├── Diagram/
├── Help_utilities/
│   └── Clear_screen.py
├── Modules/
│   ├── Unit_1.py
│   ├── Unit_2.py
│   ├── Unit_3.py
│   ├── Unit_4.py
│   └── Unit_5.py
├── Screenshots/
│   ├── Main menu.png
│   ├── Unit selection.png
│   └── Quiz result.png
├── Tests/
    └── test_functions.py
```

## How to Run

1. Make sure Python 3 is installed on your computer.
2. Open a terminal in the project folder.
3. Run the application with:

```python main.py```

On Windows, you can also use:

```py main.py```

4. Use the menu to choose a unit, start the quiz, or exit the program.

## How to Test

The project includes unit tests for the quiz logic and main menu behavior. Run the following command from the project folder:

```python -m unittest discover -s Tests```

This will execute the tests in the `Tests` folder and report if any checks fail.

## Screenshots

The project includes screenshots in the `Screenshots` folder.

| Main Menu | Unit Selection | Quiz Result |
|-----------|----------------|------------|
| ![Main Menu](Screenshots/Main%20menu.png) | ![Unit Selection](Screenshots/Unit%20selection.png) | ![Quiz Result](Screenshots/Quiz%20result.png) |

## Who Can Use This

- First-year students learning Python
- Students revising before internal or semester exams
- Teachers or seniors who want a simple example project
- Beginners who want to practice basic Python concepts

## Future Improvements

- Add more questions for each unit
- Include difficulty levels such as easy, medium, and hard
- Save quiz scores for later review
- Add a graphical user interface (GUI)

## Note

This project is intended for learning and educational practice. It can be modified and expanded for personal study or coursework use.