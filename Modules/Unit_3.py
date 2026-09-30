from Help_utilities.Clear_screen import clear_screen

def unit_3_menu():
    while True:
        clear_screen()
        print("--- UNIT 3: FUNDAMENTAL ALGORITHMS, CONTROL FLOW & FUNCTIONS ---")
        print("1. Conditionals (if, if-else, if-elif-else)")
        print("2. Iteration / Loops (while, for, break, continue)")
        print("3. Algorithm: Summation & Counting Numbers")
        print("4. Algorithm: Factorial Computation")
        print("5. Algorithm: Fibonacci Sequence Generator")
        print("6. Algorithm: Base Conversion & Reversing")
        print("7. Back to Main Menu")
        
        choice = input("\nChoose a subtopic (1-7): ")
        
        if choice == '1':
            print("\n[ LIVE DEMO: CONDITIONALS ]")
            try:
                age = int(input("Enter your age: "))
                if age < 13:
                    print("You are a child.")
                elif age < 20:
                    print("You are a teenager.")
                else:
                    print("You are an adult.")
            except ValueError:
                print("Invalid input! Please enter an integer.")
            input("\nPress Enter to continue...")
            
        elif choice == '2':
            print("\n[ LIVE DEMO: LOOPS, BREAK & CONTINUE ]")
            print("Printing numbers from 1 to 5 using a for loop, skipping 3 (continue), stopping at 5:")
            for i in range(1, 10):
                if i == 3:
                    continue  # Skip the loop
                if i == 6:
                    break     # close the loop
                print(f" Loop Item: {i}")
            input("\nPress Enter to continue.....")
            
        elif choice == '3':
            print("\n[ ALGORITHM: SUMMATION & COUNTING ]")
            limit = int(input("Enter a limit (n) to sum and count up to: "))
            total_sum = 0
            count = 0
            for i in range(1, limit + 1):
                total_sum += i
                count += 1
            print(f"Total Count of elements processed: {count}")
            print(f"Sum of numbers from 1 to {limit}: {total_sum}")
            input("\nPress Enter to continue...")
            
        elif choice == '4':
            print("\n[ ALGORITHM: FACTORIAL COMPUTATION ]")
            print("Factorial (n!) is the product of all positive integers less than or equal to n.")
            try:
                num = int(input("Enter a positive integer: "))
                if num < 0:
                    print("Factorial is not defined for negative numbers.")
                else:
                    fact = 1
                    for i in range(1, num + 1):
                        fact *= i
                    print(f"The factorial of {num}! is: {fact}")
            except ValueError:
                print("Please enter a valid integer.")

            input("\nPress Enter to continue.....")

        elif choice == '5':
            print("\n[ ALGORITHM: FIBONACCI SEQUENCE ]")
            print("Fibonacci is a sequence where each number is the sum of the two preceding ones (0, 1, 1, 2, 3, 5, 8...)")
            try:
                terms = int(input("How many terms of the Fibonacci sequence do you want? "))
                n1, n2 = 0, 1
                count = 0
                if terms <= 0:
                    print("Please enter a positive integer.")
                elif terms == 1:
                    print(f"Fibonacci sequence up to {terms}: [0]")
                else:
                    seq = []
                    while count < terms:
                        seq.append(n1)
                        nth = n1 + n2
                        n1 = n2
                        n2 = nth
                        count += 1
                    print(f"Sequence: {seq}")
            except ValueError:
                print("Please enter a valid integer.")
            input("\nPress Enter to continue...")

        elif choice == '6':
            print("\n[ ALGORITHM: REVERSING & BASE CONVERSION ]")
            try:
                num = int(input("Enter an integer to process: "))

                # Reverse the digits 
                temp = abs(num)
                rev = 0
                while temp > 0:
                    remainder = temp % 10
                    rev = (rev * 10) + remainder
                    temp //= 10

                if num < 0:
                    rev = -rev

                print(f"Reversed Number: {rev}")
                print(f"Binary Representation: {bin(num)}")
                print(f"Hexadecimal Representation: {hex(num)}")
            except ValueError:
                print("Please enter a valid integer.")

            input("\nPress Enter to continue.....")

        elif choice == '7':
             break