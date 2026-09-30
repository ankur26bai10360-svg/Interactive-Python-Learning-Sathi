from Help_utilities.Clear_screen import clear_screen
import random

def unit_4_menu():
    while True:
        clear_screen()
        print("--- UNIT 4: FACTORING METHODS ---")
        print("1. Finding square root of a number")
        print("2. Greatest Common Divisor (GCD)")
        print("3. Generation of Prime Numbers")
        print("4. Generating Pseudo-Random Numbers")
        print("5. Back to Main Menu")

        choice = input("\nChoose a subtopic (1-5): ")

        if choice == '1':
            print("\n[ ALGORITHM: SQUARE ROOT ]")
            try:
                val = float(input("Enter a number to find its square root: "))
                if val < 0:
                    print("Square root of a negative number yields an imaginary result.")
                else:
                    print(f"Square root of {val} is: {val ** 0.5:.4f}")
            except ValueError:
                print("Please enter a valid number.")
            input("\nPress Enter to continue...")

        elif choice == '2':
            print("\n[ ALGORITHM: GREATEST COMMON DIVISOR (GCD) ]")
            try:
                a = int(input("Enter first integer (a): "))
                b = int(input("Enter second integer (b): "))
                orig_a, orig_b = a, b

                while b != 0:
                    a, b = b, a % b

                print(f"The GCD of {orig_a} and {orig_b} is: {abs(a)}")
            except ValueError:
                print("Please enter valid integers.")
            input("\nPress Enter to continue...")

        elif choice == '3':
            print("\n[ ALGORITHM: PRIME NUMBER GENERATOR ]")
            try:
                limit = int(input("Find all prime numbers up to what number? "))
                primes = []

                for num in range(2, limit + 1):
                    is_prime = True
                    for i in range(2, num):
                        if i * i > num:
                            break
                        if num % i == 0:
                            is_prime = False
                            break
                    if is_prime:
                        primes.append(num)

                print(f"Prime numbers up to {limit}: {primes}")
            except ValueError:
                print("Please enter a valid integer.")
            input("\nPress Enter to continue...")

        elif choice == '4':
            print("\n[ ALGORITHM: PSEUDO-RANDOM NUMBERS ]")
            print("Computers generate random numbers using mathematical formulas.")
            print("These are called 'pseudo-random' because they are deterministic.")
            print("\nGenerating 5 pseudo-random numbers between 1 and 100:")
            print(f"Random values: {[random.randint(1, 100) for _ in range(5)]}")
            input("\nPress Enter to continue.....")

        elif choice == '5':
            break

