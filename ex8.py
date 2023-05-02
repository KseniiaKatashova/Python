#Name: Kseniia Katashova
# Exercise 2 from unit-02:
# Перевірити, чи є рядок симетричним: 

# Input: khokho
# Output:  The entered string is symmetrical

# У випадку симетрії, якщо довжина рядка парна, тоді рядок розбивається на дві половини, і виконується цикл, перевіряючи символи обох половин. 
# Якщо символи не схожі, то цикли завершується, і рядок не є симетричним, інакше рядок є симетричним.

def issymmetrical(string):
    n = len(string)
    flag =0         # marker
    
    if n%2:                     # if length is odd number
        middle = (n // 2)+ 1    # the middle index
    else:
         middle = n //2
        
    
    first_indx_1 = 0
    first_indx_2 = middle
    
    while(first_indx_1< n) and (first_indx_2 < n):
        if(string[first_indx_1] == string[first_indx_2]):
            first_indx_1 +=1
            first_indx_2 +=1
            flag =0
        else:
            print("String is not symmetrical!")
            flag =1
            break
    if flag==0:
        print("Symmetrical!")
        
        
        
    
#Check the function:
user_input = input("Please enter any word: ")
issymmetrical(user_input)

    
     
