#Name: Kseniia Katashova
# Exercise 4: Напишіть програму, що приймає довжини 2-х катетів у прямокутному трикутнику та друкує його площину. 

import colorama
from colorama import Fore
colorama.init(autoreset=True)

print("\nProgram to calculate the area of a right triangle")
print("*"*49)

a= int(input("Please enter the lenght of cathetus(a) in cm: "))

b= int(input("Please enter the lenght of cathetus(b) in cm: "))

#Calculate the area
area_of_right_tr = 0.5 * a * b
print(Fore.GREEN+f"The area of rigth triange with 2 cathetus with values {a} and {b} = {area_of_right_tr} cm")