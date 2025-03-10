# ex_10.2.py
"""Testing Car class"""
from car import Car

car1 = Car('Toyota', 2020)

print(car1, end="\n\n")


# driving faster and slower
car1.accelerate(100)
print(f'speed: {car1.speed} km/h\n')

car1.decelerate(10)
print(f'speed: {car1.speed} km/h\n')

car1.decelerate(20)
print(f'speed: {car1.speed} km/h\n')
