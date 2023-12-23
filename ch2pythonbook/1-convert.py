#!/usr/bin/python3
# convert.py
# A program to convert Celsius temps to Fahrenheit
# by: Susan Computewell

print("Celsius\tFahrenheit")
print("-------------------")
for celsius in range(0, 101, 10):
    fahrenheit = 9/5 * celsius + 32
    print(f"{celsius}\t{fahrenheit}")

