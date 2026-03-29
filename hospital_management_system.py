# Base class
class Staff:
    def get_duties(self):
        pass

    def calculate_salary(self):
        pass


# Doctor class
class Doctor(Staff):
    def get_duties(self):
        return "Diagnose patients and perform surgeries"

    def calculate_salary(self):
        return 80000

# Nurse class
class Nurse(Staff):
    def get_duties(self):
        return "Assist doctors and take care of patients"

    def calculate_salary(self):
        return 40000


# Receptionist class
class Receptionist(Staff):
    def get_duties(self):
        return "Manage appointments and patient records"

    def calculate_salary(self):
        return 25000


# Common interface to generate duty reports
staff_members = [
    Doctor(),
    Nurse(),
    Receptionist()
]

for staff in staff_members:
    print("Duty:", staff.get_duties())
    print("Salary:", staff.calculate_salary())