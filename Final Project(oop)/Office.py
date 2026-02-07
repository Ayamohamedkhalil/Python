
from Employee import Employee


class Office:
    employeesNum = 0
    
    def __init__(self, name):
       
        self.name = name
        self.employees = []

    def get_all_employees(self):
        return self.employees

    def get_employee(self, empId):
       
        for emp in self.employees:
            if emp.id == empId:
                return emp
        return None

    def hire(self, employee):
      
        if not isinstance(employee, Employee):
            print(f"Error: Can only hire Employee objects")
            return False
        
        if self.get_employee(employee.id) is not None:
            print(f"{employee.name} (ID: {employee.id}) is already employed at {self.name}")
            return False
        
        self.employees.append(employee)
        Office.employeesNum += 1
        print(f" {employee.name} has been hired at {self.name}")
        print(f"Total employees in all offices: {Office.employeesNum}")
        return True

    def fire(self, empId):
        employee = self.get_employee(empId)
        if employee is None:
            print(f"Employee with ID {empId} not found in {self.name}")
            return False
        
        self.employees.remove(employee)
        Office.employeesNum -= 1
        print(f" {employee.name} has been fired from {self.name}")
        print(f"Total employees in all offices: {Office.employeesNum}")
        return True

    def deduct(self, empId, deduction):
        employee = self.get_employee(empId)
        if employee is None:
            print(f"Employee with ID {empId} not found")
            return False
        
        employee.salary -= deduction
        print(f"Deducted {deduction} L.E. from {employee.name}'s salary")
        print(f"New salary: {employee.salary} L.E.")
        return True

    def reward(self, empId, reward):
        employee = self.get_employee(empId)
        if employee is None:
            print(f"Employee with ID {empId} not found")
            return False
        
        employee.salary += reward
        print(f"Rewarded {employee.name} with {reward} L.E.")
        print(f"New salary: {employee.salary} L.E.")
        return True

    def check_lateness(self, empId, moveHour):
        employee = self.get_employee(empId)
        if employee is None:
            print(f"Employee with ID {empId} not found")
            return False
        
        if employee.car is None:
            print(f"{employee.name} doesn't have a car to check lateness")
            return False
        
        targetHour = 9.0  
        is_late = self.calculate_lateness(
            targetHour, 
            moveHour, 
            employee.distanceToWork, 
            employee.car.velocity
        )
        
        if is_late:
            print(f"{employee.name} is LATE!")
            self.deduct(empId, 10)
            return False
        else:
            print(f" {employee.name} is ON TIME!")
            self.reward(empId, 10)
            return True

    @staticmethod
    def calculate_lateness(targetHour, moveHour, distance, velocity):
        if velocity == 0:
            return True  
        
        travel_time = distance / velocity
        
        arrival_hour = moveHour + travel_time
        
        print(f"\nLateness Calculation:")
        print(f"  Departure time: {moveHour:.2f} ({Office._format_time(moveHour)})")
        print(f"  Distance: {distance} km")
        print(f"  Velocity: {velocity} km/h")
        print(f"  Travel time: {travel_time:.2f} hours ({travel_time * 60:.0f} minutes)")
        print(f"  Arrival time: {arrival_hour:.2f} ({Office._format_time(arrival_hour)})")
        print(f"  Target time: {targetHour:.2f} ({Office._format_time(targetHour)})")
        
        return arrival_hour >= targetHour

    @classmethod
    def change_emps_num(cls, num):
        old_num = cls.employeesNum
        cls.employeesNum = num
        print(f"Total employees changed: {old_num} → {cls.employeesNum}")

    @staticmethod
    def _format_time(hour):
        h = int(hour)
        m = int((hour - h) * 60)
        period = "AM" if h < 12 else "PM"
        display_hour = h if h <= 12 else h - 12
        if display_hour == 0:
            display_hour = 12
        return f"{display_hour}:{m:02d} {period}"

    def __str__(self):
        return f"Office(Name: {self.name}, Employees Count: {len(self.employees)})"