class car:
    def __init__(self, name, fuelRate, velocity=0):
        self.name = name
        self._fuelRate = None
        self._velocity = None
        self.fuelRate = fuelRate
        self.velocity = velocity

    @property
    def velocity (self):
        return self._velocity
    
    @velocity.setter
    def velocity(Self,val):
        if 0<val<200:
            Self._velocity=val
        else:
            raise ValueError("Velocity must be between 0 and 200")    
    
    @property
    def fuelRate(self):
        return self._fuelRate
    
    @fuelRate.setter
    def fuelRate(self,f):
        if 0<f<100:
            self._fuelRate=f
        else:
            raise ValueError("FuelRate must be between 0 and 200")    

    def run(velocity,distance):
        pass

    def stop():
        pass



        
    
         