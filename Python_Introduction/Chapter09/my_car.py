from car import Car as C
from electric_car import ElectricCar as EC

my_tesla = EC('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()

my_bmw = C('BMW', 'M4', 2023)
print(my_bmw.get_descriptive_name())
