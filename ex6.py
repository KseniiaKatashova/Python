#Name: Kseniia Katashova
# Дано трикутник зі сторонами 5 см, 5 см і 6 см. Знайдіть площу і периметр трикутника.
#Use the Heron formula  A = √[s(s-a)(s-b)(s-c)]

import math
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)

print(Style.DIM+"Program to calculate the height of triange usinf Heron Formula")
print("-"*62)
a = int(input("Please enter a = "))
b = int(input("Please enter b = "))
c = int(input("Please enter c = "))

#Calculate the semi-perimeter:
s = (a + b + c) / 2

#Calculate the heigh of triangle
h = math.sqrt(s*(s-a)*(s-b)*(s-c))
print(Fore.GREEN+f"The height of triange with sides a = {a}, b = {b} and c = {c} is {h} cm ")
