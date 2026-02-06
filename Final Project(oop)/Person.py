class person:
   
    def __init__(self,name,mood,healthrate,money=0):
        self.name=name,
        self.mood="Neutral",
        self.healthrate=0,
        self.money=money,
       


    def sleep(self,hours):
        if hours<7:
            self.mood="Tired"
        elif hours> 7:
          self.mood="Lazy"
        elif hours==7:
            self.mood="Happy"   

    def eat(self,meals):
        if meals==1:
            self.healthrate="50%",
        elif meals==2:
            self.healthrate="75%",
        elif meals==3:
            self.healthrate="100%",

    def buy(self, items):
        cost_per_item = 10
        total_cost = items * cost_per_item

        if total_cost > self.money:
            print(f"{self.name} does not have enough money!")
        else:
            self.money -= total_cost
            print(f"{self.name} bought {items} item(s) for {total_cost} L.E.")
