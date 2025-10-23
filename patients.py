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
        while True: 
            patient_name = input("Enter a patient name: ")
            if patient_name: 
                pass
        