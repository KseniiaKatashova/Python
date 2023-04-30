#Name : Kseniia Katashova
#Exercise 2: Напишіть програму, що приймає ціле <число> та друкує текст : The next number for the number <число> is <число>+1. 
# The previous number for the number <число> is <число>-1. 
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

number_a = input("Enter the integer: ")

while not number_a.isdigit():
    print(Fore.RED+"Error! Please enter the whole number. Ex: 3, 90, 7564 etc")
    number_a = input("\nEnter the integer: ")
    
#Convert number to the integer type
number= int(number_a)
print(f"The next number for the number {number} is { number + 1} .")
print(f"The previous number for the number {number} is { number - 1} .")

