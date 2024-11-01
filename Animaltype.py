from Animal import Animal


class Dog(Animal):
    def care_requirements (self):
        return f"{self.name} requires daily walks, feeding thrice a day and regular check ups."
    
    def __str__(self):
        return f"Dog: {self.name}, Breed: {self.breed}, Age: {self.age}"
    
class Cat (Animal):
    def care_requirements(self):
        return f"{self.name} needs litter box cleaning, feeding twice a day"    

    def __str__(self):
        return f"Cat: {self.name}, Breed: {self.breed}, Age: {self.age}"
class Bird (Animal):
    def care_requirements(self):    
        return f"{self.name} needs a clean cage and fresh water."
    
    def __str__(self):
        return f"Bird: {self.name}, Breed: {self.breed}, Age: {self.age}"