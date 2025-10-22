# patients Side 
print("🏥🏥🏥🏥🏥.......HOSPITAL MANAGEMENT SYSTEM ......  🏥🏥🏥🏥🏥 ")
class patient: 
    def __init__(self):
        self.patiend_id = None
        self.name = None
        self.age = None
        self.gender = None
        self.contact = None
        self.address = None
        self.symptoms = None
        self.registered_date = None
        self.medical_history = None
    
    def enter__new_patient_details(self,name,age,gender,contact,address,symptoms,registered_date,medical_history): 
        self.name = input("Enter a patient full name: ")
        self.age = int(input("Enter a patient age: "))
        self.gender = input("Enter a patient gender  (male/female): ")
        self.contact = int(input("Enter  a contact number: "))
        self.address = input("Enter a patient address: ")
        self.symptoms = input("Enter a ")
        