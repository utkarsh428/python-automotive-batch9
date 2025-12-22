class SeniorCitizen:

    # 1. Constructor
    def __init__(self, age, principal, time):
        self.age = age
        self.p = principal
        self.t = time
        self.r = 8   # 8% interest

    # 2. Check age
    def check_age(self):
        return self.age >= 60

    # 3. Validate inputs (Exception handling)
    def validate(self):
        try:
            if self.p <= 0 or self.t <= 0:
                raise ValueError
            return True
        except ValueError:
            print("Error: Principal and time must be Positive")
            return False

    # 4. Calculate Compound Interest
    def calculate_ci(self):
        return self.p + (self.p * self.r * self.t) / 100

    # 5. Display result
    def display(self, ci):
        print("Compound Interest Amount:", ci)

    # 6. Main process
    def process(self):
        if not self.check_age():
            print("Only senior citizens are allowed")
            return

        if self.validate():
            ci = self.calculate_ci()
            self.display(ci)


# Object creation
account = SeniorCitizen(65, 50000, 2)
account.process()
        
