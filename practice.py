#even numbers only but in list format
# x=[1,2,3,4,5,6]
# for i in range(len(x)):
#      if i%2==0:
#          print(x[i],end=" ")


#slicing
# x=[7,8,9,2,5,6]
# k=x[:]
# print(k)

# x=[7,8,9,2,5,6]
# k=x[2:]
# print(k)

# x=[7,8,9,2,5,6]
# k=x[:4]
# print(k)

# x=[7,8,9,2,5,6]
# k=x[::-2]
# print(k)

# x=[7,8,9,2,5,6]
# k=x[-1:-3]
# print(k)

# x=[7,8,9,2,5,6]
# k=x[-4:-1]
# print(k)


#palindrome
# x=["mam"]
# for i in x:
#     if i==i[::-1]:
#         print("It is a palindrome")
#     else:
#         print("It is not a palindrome")

#another
# x="mam"
# y=x[::-1]
# if x==y:
#     print("it is a palindrome")
# else:
#     print("It is not a palindrome")

#for integer
# x=151
# y=str(x)
# z=y[::-1]
# if x==int(z):
#     print("It is a palindrome")
# else:
#     print("It is not a palindrome")


#to print even numbers using continue
# for i in range(1,11):
#     if i%2!=0:
#         continue
#     print(i)

# x=[1,5,7,3,2]
# for ele in x:
#     if ele==3:
#         break
#     print(ele)


#using while print first 10 natural numbers
# i=1
# while i<=10:
#     print(i)
#     i+=1


#palindrome using while loop
# n=152
# original=n
# rev=0
# while n>0:
#     digit=n%10
#     rev=rev*10+digit
#     n=n//10
# if rev==original:
#     print("It is a palindrome")
# else:
#     print("It is not a palindrome")


#nested loops
# for r in range(1,4):
#     for c in range(1,6):
#         print(r,c)

#nested while
# i=1
# while i<4:
#     j=1
#     while j<6:
#         print(i,j)
#         j+=1
#     i+=1


#prime or not
# n=int(input("Enter a number: "))
# count=0
# for i in range(1,n+1):
#     if n%i==0:
#         count+=1
# if count==2:
#     print("Prime number")
# else:
#     print("Not a prime number")


#without using count say if it is prime number or not, hint:use break
# n=int(input("Enter a number: "))
# for i in range(2,n):
#     if n%i==0:
#         print("Not a prime number")
#         break
#     else:
#         print("Prime number")

#from the list print only prime numbers


#calendar
# import calendar
# print(calendar.monthrange(2007,6))

# import calendar
# print(calendar.isleap(2020))


#user defined function
# def prime(n):
#     for i in range(2,n):
#         if n%i==0:
#             return "Not a prime number"
#     return "Prime number"
# print(prime(9))

#example to know diff btw print() and return
# def func():
#     print("hello")
#     return "swec"
# print(func())

#another example
# def prime(n):
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     return True
# def check(k):
#     if prime(k):
#         print("yes")
#     else:
#         print("no")
# check(5)


#local and global variables
# n=10  #global variable
# def func():
#     n=20  #local variable
#     print(n)  #prints 20
# func()
# print(n)  #prints 10


#fibbanoci
# def fibb(n):
#     if n<=1:
#         return n
#     a=0
#     b=1
#     for i in range(n+1):
#         c=a+b
#         a=b
#         b=c
#     print(b)   #or print(c)
# fibb(8)


#maximum element(1st and 2nd) without builtin function MAX
# l=[5,7,9,3,4]
# if len(l)>1:
#     maxi=l[0]
#     for ele in l:
#         if ele>maxi:
#             maxi=ele
#     print("Maximum: ",maxi)
#     max_2nd=float('-inf')
#     for ele in l:
#         if maxi>ele>max_2nd:
#             max_2nd=ele
#     print("2nd Maximum: ",max_2nd)


#raise error
# print("Start")
# try:
#     x=int(input("Enter a number upto 100:"))
#     if x>100:
#         raise ValueError(x)
# except ValueError:
#     print(x,"is out of allowed range")
# else:
#     print(x,"is within the allowed range")
# print("Stop")

#raise the exception with user defined message
# print("Start")
# try:
#     x=int(input("Enter a positive integer:"))
#     if x<0:
#         raise ValueError("You entered negative number")
# except ValueError as e:
#     print(e)
# print("Stop")


#assertion
# assert True
# print("validated")

#argumented version example
# assert "Python" in "python Programming","Validation Failed"
# print("Validation passed")


#oops
#oops class
# class Csm:
#     def students(self):
#         print("hello all")
# def kk():
#     print("hello")        
# obj1=Csm()
# obj1.students()
# kk()


#
# class Csm:
#     def __init__(self):
#         print("welcome")
# obj1=Csm()
# class Csm:
#     def __init__(self):
#        pass
#     def students(self):
#         print("hello all")
# def kk():
#     print("hello")        
# obj1=Csm()

#
# class Csm:
#     def __init__(self): #non-parameterized
#         print("welcome")
# obj1=Csm()
# class Csm:
#     def __init__(self): #default
#         pass
#     def students(self):



#parameterized constructor
# class Csm:
#     def __init__(self,name,roll): #parameterized
#         self.name=name
#         self.roll=roll
#         print(self.name,self.roll)
#     def students(self):
#         print("hello world")
# obj1=Csm("sewc",12)
# obj1.students()


#example 
# class Addition:
#     first=0
#     second=0
#     ans=0
#     def __init__(self,f,s):
#         self.f=f
#         self.s=s
#         def display(self):
#             print(self.first)
#             print(self.second)
#             print(self.ans)
#         def cal(self):
#             self.ans=self.first+self.second
# obj=Addition(100,200)
# obj.cal()
# obj.display()


#example
# class student:
#     def __init__(self,name,m1,m2,m3):
#         self.m1=m1
#         self.m2=m2
#         self.m3=m3
#     def avg(self):
#         x=(self.m1+self.m2+self.m3)/3
#         print(x)
# s1=student("swec",90,91,94)
# s2=student("college",90,88,87)
# s1.avg()
# s2.avg()

#example
# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def avg(self):    #instance method
#         x=sum(self.marks)/len(self.marks)
#         print(x)
# s1=student("swec",[90,91,94])
# s1.avg()

#
# @staticmethod
# def av(name,marks):
#     x=sum(marks)/len(marks)
#     print(x)
# s1=student("swec",[90,91,94])
# s1.avg("ss",[1,2,3])

#class method
# class Mrec:
#     Dept="CSE"
#     def Dept_name(self,name):
#         print("Instance method=",name)
#     @classmethod
#     def get_Dept(cls):
#         return cls.Dept
# m=Mrec()
# m.Dept_name("DS")
# print("Class method=",Mrec.get_Dept())

#prime numbers
# def prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
# n = int(input())
# print(prime(n))


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

#count primes
# def prime(n):
#     if n <= 1:
#         return False
#     prime = True
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
# n = int(input())
# count = 0
# for i in range(1, n):
#     if prime(i):
#         count += 1
# print(count)

#POWER OF TWO
# def powerof2(n):
#     if (n == 0):
#         return  False
#     else:
#         return n & (n-1) == 0
# n = int(input())
# print(powerof2(n))


