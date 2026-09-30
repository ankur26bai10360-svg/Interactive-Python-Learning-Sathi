# Project Statement

## Problem Statement

In the first semester, many students find Python difficult to learn, especially when they are new to programming. The notes are in one place, the practice questions are somewhere else, and there is no quick way to check whether we have really understood a topic. Because of this, revising before exams takes more time and is confusing.

I wanted to solve this by making one simple program where a student can read the important concepts of each unit and then test themselves with a quiz, all in the same place.

## Scope of the Project

**What this project does:**
- Gives a menu-based console application that runs on any computer with Python 3
- Covers the 5 units of the first-semester Python syllabus
- Has a quiz mode that checks the student's answers and shows a final score
- Has unit tests to check that the menu and quiz work properly

**What this project does not do (for now):**
- It does not have a graphical interface (only terminal based)
- It does not use a database or login system, so scores are not saved after closing the program
- It does not cover topics outside the first-semester syllabus

## Target Users

- First-year students who are learning Python for the first time
- Students who want to quickly revise before internals or semester exams
- Teachers or seniors who want a simple demo for beginners
- Anyone who wants to practice basic Python concepts

## High-Level Features

- **Main Menu:** easy navigation to all units, the quiz, or exit
- **Unit-wise Learning:** explanations for each unit (problem solving, data types, control flow, factors/GCD/primes, lists and arrays)
- **Quiz Mode:** questions with score reporting at the end
- **Simple Interface:** clean and beginner-friendly terminal screen
- **Modular Code:** separate files for each unit, quiz data, and helper functions, so the project is easy to extend
- **Testing:** unit tests for menu flow and quiz behavior