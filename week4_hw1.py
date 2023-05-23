#1. Using list comprehension, create a list of squares of all numbers
# in the range from 1 to 9.
list_of_square =[(x**2) for x in range(1,9)]
print(list_of_square)
# [1, 4, 9, 16, 25, 36, 49, 64]


#2. Using list comprehension, create a list where all the numbers are
# divisible by 5 without any remainder in the range from 0 to 100.
nums_dev_on_five = [x for x in range(0,100) if x % 5 == 0 ]
print(nums_dev_on_five)
# [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]


#3. Using list comprehension, create a list where all the numbers are
# divisible by 3 and 6 without any remainder in the range from 0 to 50.
nums_dev_on_three_and_six= [x for x in range (0,50) if x % 3 == 0 and x%6 == 0]
print(nums_dev_on_three_and_six)
#[0, 6, 12, 18, 24, 30, 36, 42, 48]


#4. Using list comprehension, create a list that contains the first letters of
# each word in the sentence 'The rocket came back from Mars':
s = 'The rocket came back from Mars'
first_letters = [word[0] for word in s.split()]
print(first_letters)
#['T', 'r', 'c', 'b', 'f', 'M']

#5. Using list comprehension, replace the letter 'a' with '#' in each word of
# the given string: "all, max, matrix, awesome, appalling, abba".
str_1 = "all, max, matrix, awesome, appalling, abba"
new_str = [word.replace('a', '#') for word in str_1.split(', ')]
print(new_str)
#['#ll', 'm#x', 'm#trix', '#wesome', '#pp#lling', '#bb#']

#6. Rewrite the code below using list comprehension:
# even_numbers = [] 
# for x in range(10):
#     if x % 2 == 0:
#         even_numbers.append(x)
# print(even_numbers) 

even_num =[ x for x in range(0,10) if x % 2 == 0]
print(even_num)
#[0, 2, 4, 6, 8]

#7. The list numbers = [121, 544, 111, 99, 77].
#Select only the numbers that are divisible by 11.
numbers = [121, 544, 111, 99, 77]
num_dev_11 = [x for x in numbers if x % 11 ==0]
print(num_dev_11)
#[121, 99, 77]

#8. Create a list comprehension that contains even numbers
# from 2 to 9998 (inclusive):

even_num = [ x for x in range(2, 9998) if x % 2 == 0]
print(even_num)


#9. To write a filter that selects the consonant letters in a sentence
sentence = 'the rocket came back from mars'
consonant_list = [letter for letter in sentence if letter not in 'aeyiou ']
print(consonant_list)
# ['t', 'h', 'r', 'c', 'k', 't', 'c', 'm', 'b', 'c', 'k', 'f', 'r', 'm', 'm', 'r', 's']


#10. To find the square of only the even numbers in the range from 0 to 9
square_of_even_num = [(x**2) for x in range(0,9) if x%2==0]
print(square_of_even_num)
#[0, 4, 16, 36, 64]

#11. To generate a multiplication table for numbers from 1 to 5
matrix = [[row * col for col in range(1, 6)] for row in range(1, 6)]
print(matrix)


#12. To generate all pairs from two tuples, a = (1, 3, 5) and b = (2, 4, 6)
a = (1, 3, 5) 
b = (2, 4, 6)
pairs = [(x,y) for x in a for y in b]
print(pairs)
# [(1, 2), (1, 4), (1, 6), (3, 2), (3, 4), (3, 6), (5, 2), (5, 4), (5, 6)]


#13. To generate all pairs from two tuples, a = (1, 3, 5) and b = (2, 4, 6), 
# satisfying the condition a > b
a = (1, 3, 5) 
b = (2, 4, 6)
new_pairs = [(x,y) for x in a for y in b if x>y ]
print(new_pairs)
#[(3, 2), (5, 2), (5, 4)]

#14. matrix = [[1, 2], [3,4], [5,6], [7,8]]
#To transpose a matrix using list comprehension
# to get result: [[1, 3, 5, 7], [2, 4, 6, 8]]
matrix = [[1, 2], [3, 4], [5, 6], [7, 8]]
new_matrix =[[row[i] for row in matrix] for i in range(len(matrix[0])) ]
print(new_matrix)
