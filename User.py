from Animal import Animal
from datetime import datetime

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.id = user_id
        self.adopted_pets = []  # List to store adopted animals
        self.records = {}  # Dictionary to store all records by animal name
        self.log = []  # List to store logs of actions

    # record for log entries
    def record_action(self, action):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.log.append(f"[{timestamp}] {action}")

    # Add an animal record
    def add_record(self, animal):
        if isinstance(animal, Animal) and animal.name not in self.records:
            self.records[animal.name] = animal
            self.adopted_pets.append(animal)
            animal.adopted = True
            action = f"{self.name} has adopted {animal.name}!"
            self.record_action(action)
            return action
        else:
            raise Exception(f"Record with name '{animal.name}' already exists or invalid type.")

    # Update an animal's information
    def update_record(self, animal_name, new_name=None, new_age=None, new_breed=None):
        if animal_name in self.records:
            animal = self.records[animal_name]
            old_info = str(animal)  
            animal.update_info(new_name, new_age, new_breed)

            # Update dictionary key if name changes
            if new_name and new_name != animal_name:
                self.records[new_name] = self.records.pop(animal_name)
            new_info = str(animal)  # Capture new information
            action = f"Updated {animal_name}'s information from '{old_info}' to '{new_info}'."
            self.record_action(action)
            return action
        else:
            raise Exception(f"No record found with name '{animal_name}'.")

    # Delete an animal record
    def delete_record(self, animal_name):
        if animal_name in self.records:
            animal = self.records.pop(animal_name)
            self.adopted_pets.remove(animal)
            animal.adopted = False
            action = f"{self.name} has returned {animal.name}."
            self.record_action(action)
            return action
        else:
            raise Exception(f"No record found with name '{animal_name}'.")

    # Method to view log entries
    def view_log(self):
        return "\n".join(self.log) if self.log else "No actions recorded."

    # Method to clear log entries
    def clear_log(self):
        self.log.clear()
        return "Log cleared."

    def __str__(self):
        return f"User: {self.name} (ID: {self.id})"