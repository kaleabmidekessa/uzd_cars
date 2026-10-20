# exnm = input('what is your name?')
# file = open('exnm.txt','w')
# file.write(exnm)
# file.close()

# with open('exnm.txt') as file:
#     line = file.read()
#     print(line)
# line = ['first line\n','second line\n','third line\n']

# with open('exnm.txt', 'w') as file:
#     file.writelines(line)

# import os

# os.path.exists

# with open('exnm.txt') as file:
#     if True:
#         print('File exists')
#     else:
#         pass

# import os

# if os.path.exists('nmk.txt'):
#     print('File exists')
# else:
#     print('File does not exist')

# from pathlib import Path

# if Path('llm.txt').exists():
#     print('File exist')
# else:
#     print('File not exist')

# try:
#     with open('missing.txt') as file:
#         pass
# except FileNotFoundError: 
#     print('looking for file')

# with open('exnm.txt') as file:
#     print(len(file.readlines()))

# with open('exnm.txt') as file:
#     line=file.read().split()

# print(len(line))

# with open('exnm.txt') as file:
#     line=file.read()

# print(len(line))

# with open('exnm.txt') as file:
#     print(file.read().count('python'))

# bros=['jk','jj','jl']

# with open('C:\\Users\\X1\\Desktop\\check.txt', 'w') as file:
#      line=file.writelines(bros)
# for i in range(2):
#     row = ''
#     for j in range(3):
#         row+='o'
#     print(row)

# def greet():
#     print('Welcome Coddy')

# greet()
# print('new session')
# greet()
# print('another session')
# greet()

# def is_even(number):
#     if number % 2 == 0:
#         print(f"{number} is even")
#     else:
#         print(f"{number} is odd")

# for i in range(15, 34):
#     is_even(i)
# for i in range(153, 219):
#     is_even(i)

# print("Welcome to FizzBuzz!")

# def fizzbuzz(number):
#     result = ""
#     if number % 3 == 0:
#         result += "Fizz"
#     if number % 7 == 0:
#         result += "Buzz"
#     if result == "":
#         result = str(number)
#     return result

# limit = int(input())

# # Play FizzBuzz
# for i in range(1, limit + 1):
#     print(fizzbuzz(i))

# print('Welcome to FizzBuzz!')
# def fizzbuzz(n):
#     result=''
#     if n%3==0 and n%7==0:
#         result+='FizzBuzz'
   
#     if n%3==0:
#         result+='Fizz'
   
#     if n%7==0:
#         result+='Buzz'
    
#     if result=='':
#         result = str(n)
#     return result

# n=int(input())
# for i in range(1,n+1):
#     print(fizzbuzz(i))

# def longest_word(text):
#     length=0
#     wordd=''

#     for i in text:
#         len_of_word=len(i)
#         if len_of_word>length:
#             length=len_of_word
#             wordd=i
#     return wordd

# sentence= 'we finally made it, hopefully not to forget it again'
# text=sentence.split()
# print(longest_word(text))
    
# def longest_word(text):
#     max_length=0
#     words=text.split()
#     wordd=''
    
#     for word in words:
#         length_of_word=len(word)
#         if length_of_word>max_length:
#             max_length=length_of_word
#             wordd=word
            
#     return wordd
    
# print(longest_word('Shrubberies are great'))


# def numbers(list):
#     for i in list:
#         print(i)
# list=[1,4,5,8,]
# numbers(list)

# def sort_by_mark(students):
#     return sorted(students, key=lambda x: x[1], reverse=False)
        

# print(sort_by_mark(sort_by_mark([[6, 'Alan'], [37, 'Ada'], [99, 'Boole'], [2, 'John']])))


# import datetime as dt
# import time
# dt.datetime.strptime(%H:%M:%S)

# numbers = [10,20,30,40,50]

# average = 0
# for num in numbers:
#     average+=num

# list = len(numbers)
# print(average/list)

# odd = []
# even = []

# for i in range(1,11):
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)

# print(f'List of Odd numbers: {odd}')
# print(f'List of Even numbers: {even}')


# lists = []
# for i in range(9,50):
#     if i % 2 == 0:
#         lists.append(i)
#     else:
#         pass

# print(lists)


# numbers = [10,20,30,40,50]

# average = 0
# count = 0
# for num in numbers:
#     average+=num
#     count+=1

# print(average/count)

# def factorial(x):
#     ''' This function returns the factorial of a given number'''
#     return x

# print(factorial(7))
# print(help(factorial))

# def is_even(list1):
#     even_num = []
#     for n in list1:
#         if n%2 == 0:
#             even_num.append(n)
#     return even_num

# list1=[2,3,42,51,62,70,5,9]
# x = is_even(list1)
# print('List of even number is:', x)
# class Fun1:
    
#     def __init__(self,loc_var):
#             self.loc_var = loc_var
#             print('value is :', loc_var)
# class Fun2(Fun1):
#      def __init__(self,loc_var):
#            super().__init__(loc_var)
#            print('Value2 is :', loc_var)


# f = Fun2(888)


# def message(first_nm, last_nm):
#     print("Hello..!", first_nm, last_nm)

# # correct use
# message("John", "Wilson")
# message("John", last_nm="Wilson")


# lis = [10,5,12,78,6,1,7,9]
# li = [1,1,1,1,1,1,1,1]
# y = map(lambda x,y:x + y, lis, li)
# print(list(y))

# import random


# for i in range(1,11):
#     x = random.randint(1,11)
#     if x == 11:
#         print(f'trial_{i}, found : {x}' )
#         break
#     else:
#         print(f'trial_{i}, {x}')

def display_person(*args):
    for i in args:
        print(i)

display_person(name="Emma", age="25")