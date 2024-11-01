class MedicalRecord:

    def __init__(self, pet, record_id):
          self.pet = pet
          self.record_id = record_id
          self.treatments = []

    def add_treatment(self, treatment):
        self.treatments.append(treatment)
        return f"Added treatment: {treatment} for {self.pet.name}."

    def view_record(self):
        treatment_list = "\n".join(self.treatments)
        return f"Medical Record for {self.pet.name}:\n{treatment_list}"

    def clear_record(self):
        self.treatments.clear()
        return f"Cleared all treatments for {self.pet.name}."