class CarManager:
    
    all_cars = {}
    total_cars = 0
    car_id = total_cars + 1

    def __init__(self):
        self._id = CarManager.car_id
        self._model =  CarManager.all_cars[CarManager.total_cars]
        self._year = CarManager.all_cars
        self._mileage = CarManager.all_cars
        self._services = []
        CarManager.all_cars[self._id] = self    # Essentially tells the all_cars 
        CarManager.total_cars += 1


    def __str__(self):
        return f'{self.make} {self.model} {self.year} {self.mileage} '

    @property
    def make(self):
        return self._make
    
    @property
    def model(self):
        return self._model
    
    @property
    def year(self):
        return self._year
    
    @property
    def mileage(self):
        return self._mileage
    
    @make.setter
    def set_make(self):
        return self._make    
    
    @model.setter
    def model(self):
        return self._model
    
    @year.setter
    def year(self):
        return self._year
    
    @mileage.setter
    def mileage(self):
        return self._mileage
    
    def __str__(self):
        return f'Vehicle: {self.make} {self.model}\nYear: {self.year}\nMiles: {self.mileage}'

@staticmethod
# Displays list of all cars to user.
def view_all():
    for cars in CarManager.all_cars:
        # print car __str__
        pass

@staticmethod
# Returns the int representing the length list hold all_cars
def count_all_cars():
    return len(CarManager.all_cars)

@staticmethod
# Takes car obj arg and appends it to class variabl all_cars
def add_to_inventory(new_car):
    CarManager.all_cars.append(new_car)

@staticmethod
def update_mileage(new_mileage):
    pass

@staticmethod
def get_int_input(prompt):
    pass

@staticmethod
def get_str_input(prompt):
    pass

@staticmethod
def display_menu():
    print({CarManager})

if __name__ == '__main__':
    # print(count_all_cars())
    # new_car = CarManager("Hyundai", 'Sonata', 2012, 123431)
    # print(new_car)
    pass