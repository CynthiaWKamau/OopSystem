from Animal import Animal
from User import User

def main():
    # Create a User
    user_name = input("Enter your name: ")
    user_id = input("Enter your ID: ")
    user = User(user_name, user_id)

    while True:
        print("\nMenu:")
        print("1. Adopt an animal")
        print("2. Update an animal's information")
        print("3. Return an animal")
        print("4. View action log")
        print("5. Clear action log")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ")

        if choice == "1":
            # Adopt an animal
            name = input("Enter the animal's name: ")
            age = int(input("Enter the animal's age: "))
            breed = input("Enter the animal's breed: ")
            animal = Animal(name, age, breed)
            try:
                print(user.add_record(animal))
            except Exception as e:
                print("Error:", e)

        elif choice == "2":
            # Update an animal's information
            animal_name = input("Enter the name of the animal to update: ")
            new_name = input("Enter new name (or press Enter to skip): ")
            new_age = input("Enter new age (or press Enter to skip): ")
            new_age = int(new_age) if new_age else None
            new_breed = input("Enter new breed (or press Enter to skip): ")

            try:
                print(user.update_record(animal_name, new_name=new_name, new_age=new_age, new_breed=new_breed))
            except Exception as e:
                print("Error:", e)

        elif choice == "3":
            # Return an animal
            animal_name = input("Enter the name of the animal to return: ")
            try:
                print(user.delete_record(animal_name))
            except Exception as e:
                print("Error:", e)

        elif choice == "4":
            # View action log
            print("\nAction Log:")
            print(user.view_log())

        elif choice == "5":
            # Clear action log
            print(user.clear_log())

        elif choice == "6":
            # Exit the program
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
