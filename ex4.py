# Number of cars available
cars = 100

# Number of seats in a car
space_in_a_car = 4.0

# Number of drivers
drivers = 30

# Number of passengers
passengers = 90

# Total cars not driven
cars_not_driven = cars - drivers

# Assigns car to driver
cars_driven = drivers

# Totals space available in cars
carpool_capacity = cars_driven * space_in_a_car

# Figures out average number of passengers per car
average_passengers_per_car = passengers / cars_driven