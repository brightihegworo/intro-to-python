# FUNCTIONS

# Difference
# Write a function, which will calculate the difference of these two numbers

def difference(num_1, num_2):
    return num_1 - num_2
#print(difference(10, 2))


# Division
# Write a function, which will divide these two numbers

def division(num_1, num_2):
    return num_1 / num_2
#print(division(10, 2))


# Function gets random number. If this number is more than ten, return the difference between 100 and this number,
# otherwise return this number multiplied by 10

def function_1(number):
    if number > 10:
        return 100 - number
    else:
        return number * 10
#print(function_1(8))


# Your function temerature_convertor gets the temperature in Fahrenheit, convert it to Celsius and return.
# Formula (32°F − 32) × 5/9 = 0°C

def temerature_convertor(fahrenheit_degree):
    return (fahrenheit_degree - 32)* 5/9
#print(temerature_convertor(67))


# Taxi Fare
# In a particular jurisdiction, taxi fares consist of a base fare of $4.00, plus $0.25 for every 140 meters travelled.
# Write a function that takes the distance travelled (in kilometers) as its only parameter and returns the total fare
# as its only result rounded by 2 digits. Write a program that demonstrates the function.

def taxi_fare(distance):
   base_fare = 4.0
   distance_in_m = distance * 1000
   fare = distance_in_m /140 * .25
   return fare + base_fare
#print(taxi_fare(10))


# examples of usage:
# taxi_fare(10) #21.86