#Name: Kseniia Katashova
# Exercise 3 from unit-02:

# Перевірити, чи є рядок паліндромом: 

# Input:amaama
# Output: The entered string is palindrome

def ispalindrome(string):
    n = len(string)
    flag =0         # marker
    

    middle = (n - 1) //2 
    first_indx_1 = 0
    last_indx = (n-1)
        
    while(first_indx_1<= middle):
        if(string[first_indx_1] == string[last_indx]):
            first_indx_1 +=1
            last_indx -=1
        else:
            flag =1
            break
    
    if flag ==0:
        print("PALINDROME!")
    else: 
        print("NOT a palindrom!")
    
#Check the function:
user_input = input("Please enter any word: ")
ispalindrome(user_input)

    
     
