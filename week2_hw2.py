# Week 2 Unit 03: Exercises 1-8:

import colorama
from colorama import Fore
colorama.init(autoreset=True)

#1. Check if the entered number is prime.    

def is_prime(n):
    if n <2:
        return False
    else:
        for a in range(2, int(n**0.5)+1):
            if (n % a)==0:
                return False         
    return True
                
#Driving code
print(is_prime(18))     #False
print(is_prime(5))      #True


#2. Write a program to unpack a tuple with several variables. 

tuple_cities = ( 'Kyiv', "Lviv", "Kharkiv", "Donetsk", "Odesa")
(s1, s2, s3, e4, s5) = tuple_cities
print(s2)
print(s1)

animals = ("cat", "dog", "guanea pig", "tiger")
(*pet, wild) = animals
print(f"Pets: {pet}")
print(f"This is a wild animal: {wild}")


#3. Write a Python program to convert a tuple to a string.

tuple_s = ( 'Hello', 'dear', 'friend', '!')

def convert_tuple_to_str(tup):
    str_1 = ''
    str_1 = ' '.join(tup)
    return str_1

print(type(convert_tuple_to_str(tuple_s)))    
print(convert_tuple_to_str(tuple_s))

#4. Check if the element is within the tuple

drinks = ('milk', 'water', 'tea', 'coffee', 'juice')

def is_in_tuple(tuple_to_check, key):
    flag =0
    for i in tuple_to_check:
        if key == i:
            return Fore.GREEN+f"Success! The '{key}'is within the tuple."
            
    return Fore.RED+f"The '{key}' is not found."

# #Driving code        
print(is_in_tuple(drinks,'cola'))
# #Output: The cola is not found 

print(is_in_tuple(drinks,'milk'))
# #Output: Yes! The milk within the tuple


#5. Revers the tuple

tuple_5 = (1, 2, 3, 4, 5, 6)

def revers_tuple(t):
    return t[::-1]

print(revers_tuple(tuple_5))
    
    
#6.Write a program to get a list sorted in ascending order by the last element
# in each tuple from a given list of non-empty tuples.

tuple_1 = (5,8,1)
tuple_2= (69,87,47,5)
tuple_3 = (22,13,2)  

def sort_list_asc_by_last_element(t1,t2,t3):
    my_list = []
    last_t1 = t1[-1]
    last_t2 = t2[-1]
    last_t3 = t3[-1]
    
    if last_t1 > last_t2 > last_t3:
        my_list.extend([t3, t2 , t1])
        
    elif last_t1 > last_t3 > last_t2:
        my_list.extend([t2, t3, t1])
        
    elif last_t2 > last_t1 >last_t3: 
        my_list.extend([t3, t1, t2])
        
    elif last_t2 > last_t3 > last_t1: 
        my_list.extend([t1, t3, t2])
        
    elif last_t3 > last_t1 > last_t2: 
        my_list.extend([t2, t1, t3])
        
    elif last_t3 > last_t2 > last_t1: 
        my_list.extend([t1, t2, t3])
        
    else:
        print("Error!")
    return my_list

# #Driving code
print(sort_list_asc_by_last_element(tuple_1,tuple_2,tuple_3))
# #Output: [(5, 8, 1), (22, 13, 2), (69, 87, 47, 5)]


#7. Check if the list is empty or not

list_1 = [1, 3, 'dog', 'apple', 'summer']
list_2 = []

def is_empty(l):
    if len(l) >=1:
        return "The list is NOT empty"
    else:
        return "The list is empty"

print(is_empty(list_2))



#8. Write a program to print the numbers from the given list after removing
# even numbers from it.

list_8 = [2, 35, 21, 7, 9, 20, 66, 13, 74, 90]
list_0 = [2,4,8,16,28]

def select_odd_num(l):
    new_list = []
    for i in l:
        if i % 2 !=0:
            new_list.append(i)
            
    if len(new_list) == 0:
        return Fore.RED+"The list is empty. No odd numbers."
    else:
        new_list.sort()
        return new_list
    
# #Driving code
print(select_odd_num(list_8))
# #Output: [7, 9, 13, 21, 35]

print(select_odd_num(list_0))
# #Output:   The list is empty. No odd numbers.        
            
            