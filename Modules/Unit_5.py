from Help_utilities.Clear_screen import clear_screen
def unit_5_menu():
    while True:
        clear_screen()
        print("--- UNIT 5: ARRAY / LIST TECHNIQUES ---")
        print("1. Array Order Reversal")
        print("2. Finding Maximum & Minimum in an Array")
        print("3. Removing Duplicates from an Indexed Array")
        print("4. Finding the K-th Smallest / Largest Element")
        print("5. Python List Operations (Slicing, Nested Lists)")
        print("6. Back to Main Menu")

        choice = input("\nChoose a subtopic (1-6): ")
        list1 = [14,8, 22, 3,14, 89,5, 22, 11]

        if choice == '1':
            print("\n[ ALGORITHM: ARRAY REVERSAL ]")
            print(f"Original list: {list1}")
            print(f"Reversed list: {list1[::-1]}")
            input("\nPress Enter to continue...")

        elif choice == '2':
            print("\n[ ALGORITHM: MAX & MIN FINDER ]")
            current_max = current_min =list1[0]
            for num in list1:
                if num > current_max:
                    current_max = num
                if num < current_min:
                    current_min = num
            print(f"List: {list1}")
            print(f"Maximum Value: {current_max}")
            print(f"Minimum Value: {current_min}")
            input("\nPress Enter to continue...")

        elif choice == '3':
            print("\n[ ALGORITHM: REMOVING DUPLICATES ]")
            unique_list = []
            for item in list1:
                if item not in unique_list:
                    unique_list.append(item)
            print(f"Original list with duplicates: {list1}")
            print(f"Cleaned list (Unique): {unique_list}")
            input("\nPress Enter to continue...")

        elif choice == '4':
            print("\n[ ALGORITHM: FINDING THE K-th ELEMENT ]")
            sorted_unique = sorted(set(list1))
            print(f"Sorted unique data points: {sorted_unique}")
            try:
                k = int(input(f"Enter the rank K (1 to {len(sorted_unique)}): "))
                if 1 <= k <= len(sorted_unique):
                    print(f"The {k}-th smallest element is: {sorted_unique[k - 1]}")
                    print(f"The {k}-th largest element is: {sorted_unique[-k]}")
                else:
                    print("Out of range bounds!")
            except ValueError:
                print("Please enter a valid integer.")
            input("\nPress Enter to continue...")

        elif choice == '5':
            print("\n[ PYTHON LIST OPERATIONS & SLICING ]")
            print(f"Target List: {list1}")
            print(f"Slice sample_list[1:4]: {list1[1:4]}")
            print(f"Slice sample_list[:3]: {list1[:3]}")
            nested = [[1, 2, 3], [4, 5, 6]]
            print(f"Nested List structure: {nested}")
            print(f"Accessing nested[1][2]: {nested[1][2]}")
            input("\nPress Enter to continue...")

        elif choice == '6':
            break