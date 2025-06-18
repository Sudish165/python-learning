class Vehicle:
    # Public function
    def displayName(self):
        return "Ford"
    
    # Protected function
    def _displayPlace(self):
        return "KTM"

    # Private function
    def __displayCar(self):
        return "BMW"

    # Public function to display private and protected data
    def displayDetails(self):
        name = self.displayName()
        place = self._displayPlace()
        car = self.__displayCar()
        return f"Name: {name}, Place: {place}, Car: {car}"

# Create object and call the public method
vehicle = Vehicle()
print(vehicle.displayDetails())
