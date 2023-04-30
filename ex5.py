#Name: Kseniia Katashova
#Exercise 5: Напишіть програму, що приймає основу і висоту трикутника, та друкує його площину

import colorama
from colorama import Fore
colorama.init(autoreset=True)

print("\nProgram to calculate the area of an isosceles triangle")
print("*"*30)

a= int(input("Please enter the base of triangle in cm: "))

h= int(input("Please enter the height in cm: "))

#Calculate the area
area = (a * h) / 2
print(Fore.GREEN+f"The area of an isosceles triange = {area} cm^2")