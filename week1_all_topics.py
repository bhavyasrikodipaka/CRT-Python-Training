'''CRT CLASSES (2nd YEAR, 1st SEM)  DATE :- 07/09/2026 (START DATE)'''

#CONDITIONAL STATEMENTS(if,elif,else)
# marks = int(input("Enter the marks: "))
# if(marks >= 90):
#     print("First Class")
# elif(marks >= 70):
#     print("Second Class")
# elif(marks >= 40):
#     print("Third Class")
# else:
#     print("Fail")


#FUNCTIONS

#*args
# def marvel(*args):
#     print(args)
# marvel("Bhavya","Poojitha")

#**kwargs
# def marvel(**args):
#      print(args)
# marvel(name1 = "Bhavya",name2 = "Poojitha")


#list :- Changes can be made(Mutable) []
#tuple :- No changes can be made(Imutable), Duplicates ()
#sets :-Unordered, No duplicates, Mutable, Indexing❌ {}
#frozenset :-Imutable, No duplicates
#dictionary :-Key:Value pairs, Mutable


#Factors
# num = int(input("Enter a number: "))
# print(f"Factors of {num}:")
# for i in range(1, num+1):
#     if(num % i == 0):
#         print(i, end = " ")

#count the no. of factors
# num = int(input("Enter a number: "))
# factor_count = 0
# print(f"No.of factors for {num}:")
# for i in range(1, num+1):
#     if(num % i == 0):
#         factor_count += 1
# print(factor_count)


#Prime number using count
# num = int(input("Enter a number: "))
# factor_count = 0
# for i in range(1, num+1):
#     if(num % i == 0):
#         factor_count += 1
# if(factor_count == 2):
#     print(f"{num} is a prime number!")
# else:
#     print(f"{num} is not a prime number!")


#PATTERNS
#1. outer loop indicates no of rows to be printed
#2. inner loop indicates no of columns (how many stars, spaces) to be printed

#printing a pattern                                   # * * * *
# n = int(input("Enter the no of rows: "))            # * * * *
# for row in range(1, n+1):     #range(0, n)          # * * * *
#     for column in range(1,n+1):     #range(n)       # * * * *
#         print("*", end = " ")
#     print()

#another pattern
# n = int(input("Enter the no of rows: "))                # *
# for row in range(n):        #range(1, n+1)              # * *
#     for column in range(row+1):       #range(row)       # * * *
#         print("*", end = " ")                           # * * * *
#     print()

#another pattern,  spaces=(n-row-1)
# n = int(input("Enter the no of rows: "))                  #       *
# for row in range(n):        #range(1, n+1)                #     * *
#     #spaces                                               #   * * *
#     for column in range(n - row - 1):                     # * * * *
#         print(" ", end = " ")
#     #stars
#     for column in range(row+1):       #range(row)
#         print("*", end = " ")
#     print()

#another pattern
# n = int(input("Enter the no of rows: "))                      #       *
# for row in range(1, n+1):        #range(1, n+1)               #     * * *
#     #spaces                                                   #   * * * * *
#     for column in range(n - row):                             # * * * * * * *
#         print(" ", end = " ")
#     #stars
#     for column in range(2 * row - 1):       #range(row)
#         print("*", end = " ")
#     print()

#another pattern
# n = int(input("Enter the no of rows: "))                 # * * * * * * *
# for row in range(0, n):        #range(1, n+1)            #   * * * * *
#     #spaces                                              #     * * *
#     for column in range(row):                            #       *
#         print(" ", end = " ")
#     #stars
#     for column in range(2 * n - 2 * row - 1):
#         print("*", end = " ")
#     print()

#another pattern
# n = int(input("Enter the no of rows: "))                # 1
# for row in range(1, n+1):        #range(n)              # 1 2
#     for column in range(row):       #range(row+1)       # 1 2 3
#         print(column + 1, end = " ")                    # 1 2 3 4
#     print()

#another pattern
# n = int(input("Enter the no of rows: "))                # 1
# for row in range(n):        #range(1, n+1)              # 2 2
#     for column in range(row + 1):       #range(row)     # 3 3  3
#         print(row + 1, end = " ")                       # 4 4 4 4
#     print()

#another pattern
# n = int(input("Enter the no of rows: "))                # 1
# for row in range(n):        #range(1, n+1)              # 0 1
#     for column in range(row + 1):       #range(row)     # 1 0 1
#         if((row + column) % 2 == 0):                    # 0 1 0 1
#             print(1, end = " ")
#         elif((row + column) % 2 == 1):
#             print(0, end = " ")
#     print()

#another pattern
# n = int(input("Enter the no of rows: "))
# for row in range(n):     #range(1, n+1)                                 # * * * *
#     for column in range(n):     #range(1, n+1)                          # *     *
#         if(row == 0 or row == n-1 or column == 0 or column == n-1):     # *     *
#             print("*", end = " ")                                       # * * * *
#         else:
#             print(" ", end = " ")
#     print()


#WHILE LOOP

#count no of digits
# num = int(input("Enter a number: "))
# digit_count = 0
# while(num > 0):
#     num = num // 10
#     digit_count += 1
# print(f"Digit Count: {digit_count}")


#reverse a number
#number only positive
# num = int(input("Enter a number: "))
# x = num
# rev = 0
# while(num > 0):
#     rem = num % 10
#     rev = (rev * 10) + rem
#     num = num // 10
# print(f"Reverse of the number {x}: {rev}")

#number negative and positive
# num = int(input("Enter a number: "))
# x = num
# if(num < 0):
#     num = abs(num)
# rev = 0
# while(num > 0):
#     rem = num % 10
#     rev = (rev * 10) + rem
#     num = num // 10
# if(x < 0):
#     print(f"Reverse of number {x}: {-rev}")
# else:
#     print(f"Reverse of number {x}: {rev}")


#take list from user
# lst = list(map(int, input("Enter: ").split()))
# print(lst)

#printing even and odd list from a list
# lst = list(map(int, input("Enter the list: ").split()))
# even = []
# odd = []
# for i in lst:
#     if(i % 2 == 0):
#         even.append(i)
#     else:
#         odd.append(i)
# print(f"Even: {even}")
# print(f"Odd: {odd}")


#print no of primes and non primes from a list
# def checkPrime(num):
#     factor_count = 0
#     for i in range(1, num + 1):
#         if(num % i == 0):
#             factor_count += 1
#     if(factor_count == 2):
#         return True
#     else:
#         return False
# def countPrimes(arr):
#     prime_count = 0
#     non_prime_count = 0
#     for num in arr:
#         if(checkPrime(num)):
#             prime_count += 1
#         else:
#             non_prime_count += 1
#     print(f"No of prime numbers: {prime_count}")
#     print(f"No of non prime numbers: {non_prime_count}")

# arr = list(map(int, input("Enter the list numbers: ").split()))
# countPrimes(arr)


#SLICING OPERATOR :- [start : stop : step] -->list and string


#MODULE :- Collection of functions
#PACKAGE :- Collection of modules with __init__.py
#LIBRARY :- Collection of packages with __init__.py


#DICTIONARY

#If you use counter list will get converted to dictionary, 
# in that dictionary key assigns as a original element and value will be its frequency

# from collections import Counter
# arr = ["peter", "tony", "tony", "thor", "thor"]
# dict1 = Counter(arr)
# print(dict1)


#Majority element
# from collections import Counter
# def majorityElement(arr):
#     n = len(arr)
#     dict1 = Counter(arr)
#     for key,value in dict1.items():
#         if(value > n//2):
#             return key
# arr = list(map(int, input("Enter the elements of list: ").split()))
# majorityElement(arr)
# print(f"Majority Element: {majorityElement(arr)}")

#Majority element II
# from collections import Counter
# def majorityelement2(nums):
#     n = len(nums)
#     dict2 = Counter(nums)
#     for key,value in dict2.items():
#         if(value > n // 3):
#             lst.append(key)
#     return lst
# nums = list(map(int, input("Enter the elements: ").split()))
# lst = []
# majorityelement2(nums)
# print(f"Majority:{lst}")


#STRINGS :- Immutable, dir(str)->to know what methods are there

#how many vowels and consonants
# s = input("Enter a string: ")
# s1 = s.lower()             #if we wont take like this
# vowel_count = 0            #  |
# cons_count = 0             #  |
# for ch in s1:              #  |------------
#     if(ch in "aeiou"):     #aeiouAEIOU <---| 
#         vowel_count += 1
#     else:
#         cons_count += 1
# print(f"No of vowels: {vowel_count}")
# print(f"No of consonants: {cons_count}")

#google password
# s = input("Enter the password: ")
# upper_count = 0
# lower_count = 0
# number_count = 0
# special_count = 0
# for ch in s:
#     if(ch.isupper()):
#         upper_count += 1
#     elif(ch.islower()):
#         lower_count += 1
#     elif(ch.isdigit()):
#         number_count += 1
#     else:
#         special_count += 1
# if(len(s) == 0):
#     print("Please enter password")
# elif(len(s) < 8):
#     print("Invalid password")
# elif(len(s) >= 8 and upper_count > 0 and lower_count > 0 and number_count > 0 and special_count > 0):
#     print("Strong password")
# else:
#     print("Weak password")


#OOPS
#1.class 2.object 3.inheritance 4.encapsulation 5.abstraction 6.polymorphism

#CONSTRUCTOR :- __init__ (used to create instance variables)
#When you create a object, constructors will run automatically
#instance variables can be allocated in different addresses with different values

#Constructor
# class Bank:
#     def __init__(self, name , amount):
#         #self.variable-->instance variable
#         self.user_name = name
#         self.balance = amount
#     def deposit(self, amount):
#         self.balance += amount
#     def withdraw(self, amount):
#         if(amount > self.balance):
#             print("Insufficient Funds")
#             return
#         self.balance -= amount
# #objectName = className
# user1 = Bank("Bhavya", 10000)
# user2 = Bank("Riya", 5000)
# user1.deposit(6000)
# print(user1.balance)
# class Animal:
#     def eat (self):
#         print("eating")


# class dog(Animal):
#     def bark(self):
#         print("barking")


# class puppy(dog):
#     def play(self):
#         print("playing")
# p=puppy()
# p.eat()
# p.bark()
# p.play()
