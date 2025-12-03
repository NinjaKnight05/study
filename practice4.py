# #-------------list comprehension  7 ----------------

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# fruits2 = ["apple", "pie", "cherry", "orange", "cherry"]

# same=[x for x in fruits if x in fruits2]
# print(same)

# #--------------------------question 1----------------------
# l=['jon snow','joffery','cersie','ned stark']

# a=input('enter the name you want to add:')

# l.append(a)
# print(l)

# b=(input('enter your best friend or importan friend name:'))
# c=int(input('enter number at which index you want to add: '))

# l.insert(c,b)
# print(l)

#--------------------------question 2------------------------

# a=(input('enter the elemensts to print by using space:'))
# list=a.split()
# print(list)

# list=[1,2,3,4,5,6,7,8,9,10]
# print(list)

# #----------------------question 3----------------------------

# l=[1,10,100,3,6,8]
# l.insert(3,59)
# print(l)
# l.append(5)
# print(l)
# print(len(l))

# #-----------------------*question 4*****************************

# newlist=[]

# for i in range (0,100):
#      if i%7==0:
#       newlist.append(i)
# print(newlist)

# #************************question 6*********************************


# list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

# newlist=[]

# for i in list:
#     if i>1:
#         is_primeNum=True
#         for j in range (2, int(i**0.5) + 1):
#          if  i%j==0:
#            is_primeNum=False
#            break
#         if is_primeNum:
#          newlist.append(i)
#          print(newlist)

# # ****************************question 5************************************

# l1=['anurag','hey','cat','bat','robert']
# l2=['sansa','robert','robb','anurag']


# differ=[x if x not in l2 else 'same as l1' for x in l1]
# print(differ)     
      
# l=[1,2,3,56,343,6,3,4,5,7,89,54]
# newl=[x for x in l if x%2==0]
# print(newl)

# tup1 = (12,4,5,6,7,88,"Hello",'World',True, False,12,4,1)
# print(tup1)
# print(type(tup1))
# print(tup1.index(2))


          


