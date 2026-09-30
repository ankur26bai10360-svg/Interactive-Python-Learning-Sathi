from Help_utilities.Clear_screen import clear_screen
from Modules.Unit_1 import unit_1_menu
from Modules.Unit_2 import unit_2_menu
from Modules.Unit_3 import unit_3_menu
from Modules.Unit_4 import unit_4_menu
from Modules.Unit_5 import unit_5_menu
from Data.Quiz import Quiz_sem1
def main():
    while True:
        clear_screen()
        print("                                                  ")
        print(" INTERACTIVE PYTHON LEARNING SATHI")
        print("                                                  ")
        print("1. Unit 1: Introduction to Problem Solving & Algorithms")
        print("2. Unit 2: Python Data, Expressions & Statements")
        print("3. Unit 3: Control Flow, Loops & Fund. Algorithms")
        print("4. Unit 4: Factoring Methods (GCD, Primes, math)")
        print("5. Unit 5: Array & List Processing Techniques")
        print("6. Quiz & Scores")
        print("7. Exit Application")
        print("==================================================")

        main_choice = input("\nSelect a Unit syllabus you want to study (1-6): ")

        if main_choice == '1':
            unit_1_menu()
        elif main_choice == '2':
            unit_2_menu()
        elif main_choice == '3':
            unit_3_menu()
        elif main_choice == '4':
            unit_4_menu()
        elif main_choice == '5':
            unit_5_menu()
        elif main_choice == '6':
            Quiz_sem1()
        elif main_choice == '7':
            print("\nThank you for using the Python Learning Companion! Happy Coding!\n")
            break
        else:
            print("\nInvalid choice! Please select an option between 1 and 6.")
            input("Press Enter to try again...")


if __name__ == "__main__":
    main()




