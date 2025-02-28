class Vehicle:
    def __init__(self, brand, model, year, rental_price_per_day):
        self.brand = brand
        self.model = model
        self.year = year
        self.__rental_price_per_day = rental_price_per_day

    def display_info(self):
        print(f"{self.brand} {self.model}, Year: {self.year}, Rental Price: {self.__rental_price_per_day}$/day")

    def calculate_rental_cost(self, days):
        return self.__rental_price_per_day * days

    def get_rental_price(self):
        return self.__rental_price_per_day

    def set_rental_price(self, new_price):
        if new_price > 0:
            self.__rental_price_per_day = new_price
        else:
            print("Rental price must be positive!")

class Car(Vehicle):
    def __init__(self, brand, model, year, rental_price_per_day, seating_capacity):
        self.seating_capacity = seating_capacity
        super().__init__(brand, model, year, rental_price_per_day)

    def display_info(self):
        print(f"Car: {self.brand} {self.model}, Year: {self.year}, Seats: {self.seating_capacity}, Rental Price: {self.get_rental_price()}$/day")

class Bike(Vehicle):
    def __init__(self, brand, model, year, rental_price_per_day, engine_capacity):
        self.engine_capacity = engine_capacity
        super().__init__(brand, model, year, rental_price_per_day)

    def display_info(self):
        print(f"Bike: {self.brand} {self.model}, Year: {self.year}, Engine: {self.engine_capacity}cc, Rental Price: {self.get_rental_price()}$/day")

def show_vehicle_info(vehicle):
    vehicle.display_info()

cars = [
    Car("Toyota", "Corolla", 2022, 50, 5),
    Car("Honda", "Civic", 2021, 55, 5),
    Car("Ford", "Focus", 2020, 45, 5),
    Car("BMW", "3 Series", 2023, 80, 5),
    Car("Mercedes", "C-Class", 2022, 90, 5)
]

bikes = [
    Bike("Yamaha", "R1", 2019, 30, 998),
    Bike("Honda", "CBR600RR", 2020, 25, 599),
    Bike("Ducati", "Panigale V4", 2022, 60, 1103),
    Bike("Kawasaki", "Ninja ZX-10R", 2021, 40, 998),
    Bike("Suzuki", "GSX-R750", 2020, 35, 750)
]

while True:
    choice = input("Do you want to rent a Car or a Bike? (Car/Bike): ").strip().lower()

    if choice == "car":
        print("Available Cars: ")
        index = 1
        for car in cars:
            print(f"{index}. {car.brand} {car.model} ({car.year}) - {car.get_rental_price()}$/day")
            index += 1
        selection = int(input("Choose a car (1-5): ")) - 1
        if 0 <= selection < len(cars):
            selected_vehicle = cars[selection]
            break
        else:
            print("Invalid selection, please try again.")
    
    elif choice == "bike":
        print("Available Bikes: ")
        index = 1
        for bike in bikes:
            print(f"{index}. {bike.brand} {bike.model} ({bike.year}) - {bike.get_rental_price()}$/day")
            index += 1
        selection = int(input("Choose a bike (1-5): ")) - 1
        if 0 <= selection < len(bikes):
            selected_vehicle = bikes[selection]
            break
        else:
            print("Invalid selection, please try again.")
    
    else:
        print("Invalid choice, please try again.")

show_vehicle_info(selected_vehicle)

days = int(input("Enter the number of rental days: "))
print(f"Total rental cost: {selected_vehicle.calculate_rental_cost(days)}$")
