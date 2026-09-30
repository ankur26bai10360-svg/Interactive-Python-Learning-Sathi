from Help_utilities.Clear_screen import clear_screen
def unit_1_menu():
    while True:
        clear_screen()
        
        print("  UNIT 1: INTRODUCTION TO PROBLEM SOLVING & ALGORITHMS    ")
       
        print("1. Top-Down Design Concept")
        print("2. What is an Algorithm & Flowchart?")
        print("3. Pseudo-code Example")
        print("4. Program Verification & Efficiency (Time Complexity)")
        print("5. Back to Main Menu")
        
        choice = input("\nChoose a subtopic (1-5): ")
        
        if choice == '1':
            print("\n[ CONCEPT: TOP-DOWN DESIGN ]")
            print("Top-Down Design (Modular Programming) means breaking a complex problem")
            print("down into smaller, manageable sub-problems (tasks).")
            print("\nExample: To build a Calculator, we break it into:")
            print(" - Task 1: Get user input")
            print(" - Task 2: Perform calculation (Add/Subtract/etc.)")
            print(" - Task 3: Display result")
            input("\nPress Enter to continue.....")
            
        elif choice == '2':
            print("\n[ CONCEPT: ALGORITHMS & FLOWCHARTS ]")
            print("- Algorithm: A step-by-step set of instructions to solve a problem.")
            print("- Flowchart: A visual/graphical representation of an algorithm using shapes.")
            print("  * Oval = Start/End")
            print("  * Parallelogram = Input/Output")
            print("  * Rectangle = Process/Calculation")
            print("  * Diamond = Decision (If/Else)")
            input("\nPress Enter to continue...")
            
        elif choice == '3':
            print("\n[ CONCEPT: PSEUDO-CODE ]")
            print("Pseudo-code is an informal, human-readable way to write code before")
            print("actually translating it into a programming language like Python.")
            print("\n   Pseudo-code to find the largest of two numbers   ")
            print("START")
            print("  INPUT num1, num2")
            print("  IF num1 > num2 THEN")
            print("    PRINT num1 is larger")
            print("  ELSE")
            print("    PRINT num2 is larger")
            print("END")
            input("\nPress Enter to continue...")
            
        elif choice == '4':
            print("\n[ CONCEPT: PROGRAM VERIFICATION & EFFICIENCY ]")
            print("- Verification: Checking if the program solves the problem correctly")
            print("  for all valid inputs (Testing boundary cases).")
            print("- Efficiency: How well code performs regarding Time (speed) and Space (memory).")
            print("  We measure this using Big-O Notation (e.g., O(1), O(n), O(n²)).")
            input("\nPress Enter to continue...")
            
        elif choice == '5':
            break