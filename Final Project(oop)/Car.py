
class Car:
   
    
    def __init__(self, name, fuelRate, velocity=0):
        self.name = name
        self._fuelRate = None
        self._velocity = None
        self.fuelRate = fuelRate  # Uses setter for validation
        self.velocity = velocity   # Uses setter for validation

    @property
    def velocity(self):
        return self._velocity
    
    @velocity.setter
    def velocity(self, val):
        if 0 <= val <= 200:
            self._velocity = val
        else:
            raise ValueError("Velocity must be between 0 and 200")
    
    @property
    def fuelRate(self):
        return self._fuelRate
    
    @fuelRate.setter
    def fuelRate(self, f):
        
        if 0 <= f <= 100:
            self._fuelRate = f
        else:
            raise ValueError("FuelRate must be between 0 and 100")

    def run(self, velocity, distance):
       
        self.velocity = velocity
        remaining_distance = distance
        
        print(f"\n{self.name} starting journey: {distance}km at {velocity}km/h")
        print(f"Initial fuel rate: {self.fuelRate:.2f}%")
        
        while remaining_distance > 0 and self.fuelRate > 0:
            distance_chunk = min(10, remaining_distance)
            
            if self.fuelRate > 0:
                remaining_distance -= distance_chunk
                self.fuelRate = max(0, self.fuelRate - 10)
                
                print(f"Traveled {distance_chunk}km - Fuel rate now: {self.fuelRate:.2f}%")
            else:
                break
        
        self.stop(remaining_distance)

    def stop(self, remaining_distance=0):
       
        self.velocity = 0
        
        if remaining_distance <= 0:
            print(f"\n{self.name} arrived at destination successfully!")
        else:
            print(f"\n {self.name} stopped! Out of fuel.")
            print(f"  Remaining distance to destination: {remaining_distance:.2f}km")

    def __str__(self):
        return f"Car(Name: {self.name}, Fuel: {self.fuelRate}%, Velocity: {self.velocity} km/h)"