from Vehicle import Vehicle

class Exotics(Vehicle):
    exotic_brands = ['Ferrari', 'Lamborghini', 'Porsche']
    def __init__(self,brand,model,year,doors,exotic_type):
        super().__init__(brand,model,year,doors)
        self.exotic_type = exotic_type
    
    def is_exotic(self):
        '''Determins if the car is considered an exotic car'''
        if self.brand in Exotics.exotic_brands:
            return f"{self.brand} is an exotic car!"
        return f"{self.brand} is NOT an exotic car!"