from Help_utilities.Clear_screen import clear_screen

def unit_2_menu():
	while True:
		clear_screen()
		print("   UNIT 2: PYTHON DATA, EXPRESSIONS, AND STATEMENTS   ")
		print("1. Interactive Mode vs Script Mode")
		print("2. Variables, Data Types, and Operators")
		print("3. Operator Precedence (PEMDAS)")
		print("4. Function Structure (Parameters & Arguments)")
		print("5. Back to Main Menu")

		choice = input("\nChoose a subtopic (1-5): ")

		if choice == '1':
			print("\n[ INTERACTIVE VS SCRIPT MODE ]")
			print("- Interactive Mode: You type code one line at a time in the REPL (>>>)")
			print(" and Python executes it instantly. Great for testing single lines.")
			print("- Script Mode: You save your code in a file (like this script.py file)")
			print(" and run the whole thing together. Best for real programs.")
			input("\nPress Enter to continue...")

		elif choice == '2':
			print("\n[ Test : VARIABLES & DATA TYPES ]")
			x = 10  # Inte
			y = 4.12  # Floa
			name = "Python"  # Stri
			is_fun = True  # Bool
			print(f"Variable x = {x} is of type {type(x)}")
			print(f"Variable y = {y} is of type {type(y)}")
			print(f"Variable name = '{name}' is of type {type(name)}")
			print(f"Variable is_fun = {is_fun} is of type {type(is_fun)}")
			print("\n[ LIVE DEMO: ARITHMETIC OPERATORS ]")
			print(f"Addition (10 + 3): {10 + 3}")
			print(f"Modulus/Remainder (10 % 3): {10 % 3}")
			print(f"Exponent/Power (2 ** 3): {2 ** 3}")
			print(f"Floor Division (10 // 3): {10 // 3}")
			input("\nPress Enter to continue...")

		elif choice == '3':
			print("\n[ LIVE DEMO: OPERATOR PRECEDENCE ]")
			print("Python follows PEMDAS (Parentheses, Exponents, Multiplication/Division, Addition/Subtraction).")
			expression = 5 + 3 * 2
			print(f"Expression: 5 + 3 * 2 = {expression} (Multiplication happens first)")
			expression_with_parentheses = (5 + 3) * 2
			print(f"Expression: (5 + 3) * 2 = {expression_with_parentheses} (Parentheses happen first)")
			input("\nPress Enter to continue...")

		elif choice == '4':
			print("\n[ CONCEPT: FUNCTIONS, PARAMETERS, & ARGUMENTS ]")
			print("A function is a reusable block of code.")
			print("- Parameter: The placeholder variable defined inside the function header.")
			print("- Argument: The actual value passed into the function when calling it.")

			def greet_user(username):
				return f"Hello, {username}! Welcome to Unit 2."

			my_name = input("\nEnter your name: ")
			message = greet_user(my_name)
			print(f"Output: {message}")
			input("\nPress Enter to continue...")

		elif choice == '5':
			break