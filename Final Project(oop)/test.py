class Mammal:
    def eat(self):
        print("Mammal: Consuming food for energy")
        
    def breathe(self):
        print("Mammal: Breathing oxygen")

class Human:
    def eat(self):
        print("Human: Eating with utensils")
        
    def speak(self):
        print("Human: Speaking language")

class Employee(Human, Mammal):
    def work(self):
        print("Employee: Working on tasks")

# Test
emp = Employee()
emp.eat()
