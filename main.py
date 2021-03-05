# Python program to convert temperature from
# Fahrenheit to Kelvin

# Function to convert temperature
def Fahrenheit_to_Kelvin(F):
    return 237.5 + ((F-32.0) * (5.0/9.0))

# Driver Function
F = 100
print("Temperature in Kelvin from F ( K ) = {:.3f}"
      .format(Fahrenheit_to_Kelvin(F)))

def Kelvin_to_Fahrenheit(K):
    return (((K - 237.15) * 9) / 5) + 32
K = 1000
print("Temperature in Fahrenheit from K = {:.3f}"
      .format(Kelvin_to_Fahrenheit(K)))

def Fahrenheit_to_Celsius(F):
    return (F - 32) * 5/9
F = 100
print("Temperature in Celsius  from F = {:.3f}"
      .format(Fahrenheit_to_Celsius(F)))

def Celsius_to_Fahrenheit(C):
    return (C * 9/5) + 32
C = 100
print("Temperature in Fahrenheit from C = {:.3f}"
      .format(Celsius_to_Fahrenheit(C)))

def Celsius_to_Kelvin(C):
    return C + 273.15
C = 200
print("Temperature in Kelvin from C = {:.3f}"
      .format(Celsius_to_Kelvin(C)))

def Kelvin_to_Celsius(K):
    return K - 273.15
K = 400
print("Temperature in Celsius from K = {:.3f}"
      .format(Kelvin_to_Celsius(K)))