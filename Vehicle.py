class Vehicle:
    def __init__(self, brand, model, year):
        self._brand = brand
        self._model = model
        self._year = year

    def display_info(self):
        """Abstract method to display vehicle info."""
        return f"{self._brand} {self._model} ({self._year})"
    
    def honk(self):
        """A general honk sound for all vehicles."""
        return "Beep beep!"
    
    def fuel_up(self):
        return "Full tank" 

    def windshield_fluid(self):
        return f"Windshield fluid empty. Please consult owners manual for proper filling."
    
    def brake(self):
        print("Braking the car.")
    


