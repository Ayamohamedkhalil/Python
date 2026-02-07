
from Person import person
from Car import Car


class Employee(person):
  
    def __init__(self, name, emp_id, email, salary, distanceToWork, car=None, money=0):
       
        super().__init__(name, money)
        self.id = emp_id
        self.car = car
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork

    def work(self, hours):
        
        if hours < 8:
            self.mood = "Lazy"
        elif hours > 8:
            self.mood = "Tired"
        else:  # hours == 8
            self.mood = "Happy"
        
        print(f"{self.name} worked for {hours} hours and feels {self.mood}")

    def drive(self, distance, velocity):
       
        if self.car is None:
            raise ValueError(f"{self.name} doesn't have a car!")
        
        print(f"\n{self.name} is driving {self.car.name}...")
        self.car.run(velocity, distance)

    def refuel(self, gasAmount=100):
        
        if self.car is None:
            raise ValueError(f"{self.name} doesn't have a car!")
        
        old_fuel = self.car.fuelRate
        try:
            self.car.fuelRate = min(100, self.car.fuelRate + gasAmount)
            print(f"{self.name} refueled {self.car.name}: {old_fuel:.1f}% → {self.car.fuelRate:.1f}%")
        except ValueError as e:
            print(f"Refuel error: {e}")

    def send_mail(self, to_email, subject, message):
       
        print(f"\n--- Email Sent ---")
        print(f"From: {self.email}")
        print(f"To: {to_email}")
        print(f"Subject: {subject}")
        print(f"Message: {message}")
        print(f"------------------\n")


    def __str__(self):
        return (
            f"Employee(Name: {self.name}, ID: {self.id}, "
            f"Email: {self.email}, Salary: {self.salary}, "
            f"Distance to Work: {self.distanceToWork} km)"
        )     