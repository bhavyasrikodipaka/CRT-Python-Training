'''CRT CLASSES (2nd YEAR, 1st SEM)  DATE :- 09/11/2026 (START DATE)'''
# x ='''Sridevi'''
# print(type(x))

# for i in range(1, 101):
#     if (i % 3 == 0 & i % 5 == 0):
#         print("FizzBuzz")
#     elif (i % 3 == 0):
#         print("Fizz")
#     elif(i % 5 == 0):
#         print("Buzz")
#     else:
#         print(i)

# def add():
#     p1 = 500
#     p2 = 300
#     t = p1 + p2
#     print(f"total = {t}")
# add()

# def operations(a, b):
#     print(a + b)
#     print(a - b)
#     print(a * b)
#     if (b != 0):
#         print(a / b)
#     else:
#         print("Undefined")
#     print(a ** b)
#     if (b != 0):
#         print(a // b)
#     else:
#         print("Undefined")
# operations(1,0)

# class CSM():
#     s1 = "vaishnavi"
#     s2 = "vedha"
#     s3 = "sreenidhi"
# Hod = CSM()
# print(Hod.s3)
# print(CSM.s3)

# class MOVIES():
#     def Ramayana(self):
#         print("Mythology")
#     def OG(self):
#         print("Action")
#     def Conguring(self):
#         print("Horror")
# obj = MOVIES()
# obj.Conguring()

# name = "Bhavya"
# count = 0
# for i in name:
#     if (ord(i) % 2 == 0):
#         count += ord(i)
# print(count)

# LEAP YEAR
# year = int(input("Year: "))
# if (year % 400 == 0 & year % 4 == 0):
#     print("It is a leap year!")
# else:
#     print("It is not a leap year!")

# n = 5
# x = 7
# print((n>5) and (x>n))

# print(13 ^ 7 & 5)

# print(5 << 1)  
# left shift: x * 2 ** (k) -->generic formula
# right shift: x // 2 ** k -->generic formula

# CHECK kth-bit
# n = 4
# k = 2
# if (n & (1 << k)):
#     print(True)
# else:
#     print(False)

#EVEN OR ODD#
# n = 14
# if ((n & 1) == 0):
#     print("Even")
# else:               # n & 1 == 1
#     print("Odd")

#LeetCode #231 --> POWER OF TWO
# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
#         if (n == 0):
#             return  False
#         else:
#             return n & (n-1) == 0

#another method
# n = int(input())
# if n & (n - 1) == 0:
#     print(True)


#2 power - msb 1
#even - lsb 0
#odd - lsb 1


#LeetCode #191 --> NO.OF 1(SET) BITS
# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         if (n == 0):
#             return 0
#         c = 0
#         while (n != 0):
#             n = n & (n - 1)
#             c += 1
#         return c

#SET RIGHTMOST UNSET BIT
# def setBit(n):
#     return n | (n + 1)
# print(setBit(15))

#COUNTING NUMBERS
# n = int(input("Enter a number: "))
# c = 0
# while n > 0:
#     n = n // 10
#     c += 1
# print(c)

#TO PRINT ONLY ODD NUMBERS
# n = int(input("Enter a number: "))
# while n > 0:
#     dig = n % 10
#     if dig % 2 != 0:
#         print(dig)
#     n = n // 10

#TO PRINT HIGHEST NUMBERS
# n = int(input("Enter a number: "))
# largest = 0
# while n > 0:
#     dig = n % 10
#     if dig > largest:
#         largest = dig
#     n = n // 10
# print(largest)

#PALINDROME FOR NUMBERS
# n = int(input("Enter number: "))
# n1 = n
# rev = 0
# while (n > 0):
#     rem = n % 10
#     rev = (rev * 10) + rem
#     n = n // 10
# if (n1 == rev):
#     print("It is a palindrome")
# else:
#     print("It is not a palindrome")

#PALINDROME FOR STRING
# n = input("Enter number: ")
# if n == n[::-1]:
#     print("It is a palindrome")
# else:
#     print("It is not a palindrome")

#ARMSTRONG
# n = int(input("Enter a number: "))
# n1 = n
# n2 = n
# c = 0
# sum = 0
# while n > 0:
#     n = n // 10
#     c += 1
# while n1 > 0:
#     dig = n1 % 10
#     sum += dig ** c
#     n1 = n1 // 10
# if n2 == sum:
#     print(f"{n2} is an armstrong")
# else:
#     print(f"{n2} is not an armstrong")

#PERFECT NUMBER #Leetcode 
# def perfectno(n):
#     sum = 0
#     for i in range(1, 28):
#         if n % i == 0:
#             sum += i
#     if sum == n:
#         return True
#     else:
#         return False
# n = 28
# print(perfectno(n))

#FACTORIAL
# n = int(input("Enter a number: "))
# fact = 1
# for i in range(1, n+1):    #range(n, 0, -1)
#     fact *= i
# print(f"Factorial: {fact}")

#RECURSION
# def sumi(n):
#     if n == 0:
#         return
#     print(n)
#     return (sumi(n-1))
# sumi(5)

# def sumi(n):
#     if n == 0:
#         return
#     sumi(n - 1)
#     print(n)
# sumi(5)

#function terminates at 2 points
#   -after complition of all points
#   -after executing of the return statement

#FACTORIAL USING RECURSION
# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n - 1)
# print(factorial(5))

#PRIME NUMBER
# def prime(n):
#     if n <= 1:
#         return "Not a prime"
#     for i in range(2, n):
#         if n % i == 0:
#             return "Not a prime"
#     else:
#         return "Prime"
# n = int(input("Enter a number: "))
# print(prime(n))

#another method
# def prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
# n = int(input())
# print(prime(n))

#another method
# def prime(n):
#     if n <= 1:
#         print("false")
#     prime = True
#     for i in range(2, n):
#         if n % i == 0:
#             prime = False
#     if prime:
#         print("true")
#     else:
#         print("false")
# n = int(input())
# prime(n)

#COUNTING PRIME NUMBERS
# def prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
# def countprime(n1):
#     count = 0
#     for x in range(2, n1 + 1):
#         if prime(x):
#             count += 1
#     return count
# n1 = int(input("Enter a number: "))
# print(f"Total prime numbers: {countprime(n1)}")

#another method
# n = int(input("number: "))
# count = 0
# for i in range(2, n):
#     prime = True
#     for j in range(2, i):
#         if i % j == 0:
#             prime = False
#     if prime:
#         count += 1
# print(count)

#another method
# def prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     else:
#         return True
# n = int(input("Enter a number: "))
# count = 0
# for i in range(1, n):
#     if prime(i):
#         count += 1
# print(count)

#Sieve of Erosthenes

#COUNTING PRIMES #Leetcode 182 #Sieve of Erosthenes
# class Solution:
#     def countPrimes(self, n: int) -> int:
#         if n <= 1:
#             return 0
#         p = [True] * n
#         p[0] = False
#         p[1] = False
#         c = 0
#         for i in range(2, n):
#             if p[i]:
#                 c += 1
#             for j in range(i * i, n, i):
#                 p[j] = False
#         return c

#TAKE INPUT IN ONE LINE
#a,b = map(int,input().split())
#print(a,b)

#REVERSE A NUMBER
# n = int(input())
# rev = 0
# while (n > 0):
#     rem = n % 10
#     rev = (rev * 10) + rem
#     n //= 10
# print(rev)

#GCD
# import math
# print(math.gcd(6, 18))

#DIVISORS
# n = int(input("Enter a number: "))
# for i in range(1, n +1):
#     if n % i == 0:
#         print(i)

#LCM
# import math
# print(math.lcm(6, 8))

def gcd(a, b):
    small = a
    if b < small:
        small = b
    gcd = 1
    for i in range(1, small + 1):
        if a % i == 0 and b % i == 0:
            gcd = i
    return gcd