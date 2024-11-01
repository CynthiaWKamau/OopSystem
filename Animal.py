class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species
        self.adopted = False  # Track if the animal has been adopted

    def update_info(self, name=None, age=None, species=None):
        if name:
            self.name = name
        if age:
            self.age = age
        if species:
            self.species = species
        return f"Information updated for {self.name}."

    def __str__(self):
        status = "adopted" if self.adopted else "available"
        return f"{self.species.capitalize()}: {self.name}, Age: {self.age}, Status: {status}"