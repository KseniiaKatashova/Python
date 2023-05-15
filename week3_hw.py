import colorama
from colorama import Fore
colorama.init(autoreset=True)

#1. Write a program to find the line in the file 'sale.txt' and print this line.

def seach_item(file_path, item):

    with open(file_path, 'r') as f:
        content= f.readlines()
        
        for line in  content:
            if item in line:
                return print(Fore.GREEN +f"RESULT: {line} ")
                
               

        print(Fore.RED + f"The item '{item}' is not within the file '{f.name}'!")


        
# #Driving Code   
seach_item('sales.txt', 'Ceylon')




#2. You have a file with this content: Peter Piper picked a peck of pickled
# peppers. A peck of pickled peppers Peter Piper picked. Where's the peck of
# pickled peppers Peter Piper picked.
# You should enter new sentence: If Peter Piper picked a peck of pickled peppers) after the second sentence. 

with open('week3_e2.txt', 'r+') as f:
    file = f.readlines()
    for index,line in enumerate(file):                  #enumerate() function is used to iterate over the lines of the file
        if 'A peck of pickled peppers Peter Piper picked.\n' in line:
            file.insert(index+1, 'If Peter Piper picked a peck of pickled peppers.\n')
            break
    f.seek(0)
    f.writelines(file)
    




