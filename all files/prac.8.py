
# def funcs():
#   l=[1,2,3,4,5,3,2,1,34,5]
#   s=set(l)
#   print(s)
# funcs()

#--------------------

# def calculate(*a):
#     sum=1
#     for i in a:
#         sum*=i
#     return sum
# print(calculate(2,3,5,8,4))

#----------------------------------

# num=int(input('enter num:'))
# squaren= lambda num:num**2
# print(squaren(num))

#----------------------------

# dict1=[{'name':'jon-snow','family':'starks'}]

# a=input('enter name:')
# b=input('enter family:')

# dict1.append({
#     'name':a,
#     'family':b
# })

# def kwargsss(**a):
#  for i,j in enumerate(dict1):
#   print(i+1,j)

# print(kwargsss())

#--------------------

# import random

# def otpgenerate():
#   for i in range(0,6):
#     print(random.randint(0,9),end=' ')

# otpgenerate()

# a=int(input('enter the marks:'))

# def grade(a):
#     if a>91 and a<=100:
#         print("Grade-A")
#     elif a>81 and a<=90:
#         print('Grade-B')
#     elif a>71 and a<=80:
#         print('Grade-C')
#     elif a>61 and a<=70:
#         print('Grade-D')
#     else:
#         print('Fail')

# print(grade(a))