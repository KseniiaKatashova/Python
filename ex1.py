#Name : Kseniia Katashova
# Exersice 1: Дано кількість діб n. Пройшло m хвилин. Скільки годин та хвилин показує електронний годинник у даний момент.
# Програма має надрукувати два числа: кількість годин (від 0 до 23) та кількість хвилин (від 0 до 59). 

n_days = int(input("\nPlease enter the number of days: "))

n_minutes= int(input("Please enter the number of minutes: "))
print("_"*30)


#Convert hours to minutes
total_in_minutes = (n_days * 60 * 24) + n_minutes

# # Calculate the current time
new_n_hours = (total_in_minutes // 60 ) 
while  new_n_hours > 23:
    new_n_hours -=24
    
new_n_minutes = total_in_minutes % 60

print(f"Current time is : {new_n_hours} hours and {new_n_minutes} minutes\n")

