
# for i in  range(0,51):
#   if i%3==0 and  i%5==0:
#       print('fizzbuzz',i) 
#   elif i%3==0:
#       print('fizz',i)
#   elif i%5==0:
#       print('buzz',i)
#   else :
#       print('Alone',i)

 #***********************************

# a=input('enter child name:')

# s1=int(input('enter the score you want to give him(0-100):'))

# if s1>=90 and s1<=100:
#     print('A')
# elif s1>=80 and s1<=89:
#     print('C')
# elif s1>=70 and s1<=79:
#     print('D')
# elif s1>=60 and s1<=69:
#     print('E')
# else:
#     print('you Failed' , a ,' dummy')     
   

#***********************************     
# n=[]
# for i in range(0,21):
#     if i%2==0:
#       n.append(i)
# print(n)

#**********************************

# year=int(input('enter the Year:'))

# if (year%400==0) or (year%4==0 and year%100!=0):
#     print('it is a leap year')
# else:
#     print('no leap year')    

#**********************************
# print('fill 0-90 degrees')
# a=int(input('enter the 1 angle degree:'))
# b=int(input('enter the 2 angle degree:'))
# c=int(input('enter the 3 angle degree:'))

# if a==b==c:
#     print('equilateral trianle')
#     if a<90 and b<90 and c<90:
#         print('Also acute angle')
# elif (a==b) or  (b==c)  or (c==a) :
#     print('Isoscales trianle')
#     if a<90 and b<90 and c<90:
#         print('Also acute angle')
#     elif  a==90 or b==90 or c==90:
#         print('also right angle tirangle')
#     elif a>90 or b>90 or c>90:
#         print('also obtuse angle') 
# elif (a!=b)and (b!=c) and (c!=a) :
#     print('scalene triangle')
#     if a<90 and b<90 and c<90:
#         print('Also acute angle')
#     elif a==90 or b==90 or c==90:
#         print('also right angle tirangle')
#     elif a>90 or b>90 or c>90:
#         print('obtuse angle')

#**********************************

# a=int(input('enter a number:'))

# if a>1:
#     print('positive number')
# elif a<0:
#     print('negative number')
# else:
#     print('its zero')


#**********************************
# a=int(input('create a password:'))

# for i in a:
#     if len(a)<8:
#         print('password should be atleast 8 chracters long'

#**********************************
# bmi=float(input('enter the body mass index:'))

# if bmi<18.5:
#     print('under weight')
# elif bmi>=18.5 and bmi<=24.9:
#     print('normal')
# elif bmi>25 and bmi<=29:
#     print('overweight')
# else:
#    print ('obesity')

#**********************************

# a=int(input('enter a number 0-7 for days:'))

# if a==1:
#     print('monday')
# elif a==2:
#     print('tuesday')
# elif a==3:
#     print('wednesday')
# elif a==4:
#     print('thursday')
# elif a==5:
#     print('friday')
# elif a==6:
#     print('saturday')
# elif a==7:
#     print('sunday')
# else:
#    print('bakchodi mat kr')

#**********************************

# price=int(input('enter the price:'))

# if price>=1000:
#     discount=price *10/100
#     final_price=price-discount
#     print('price is',final_price,'with 10 % discount applied')
# elif price>=500 and price<1000:
#     discount=price *5/100
#     final_price=price-discount
#     print('price is',final_price,'with 5 % discount applied')
# elif price<500:
#      print('no discount ')

#**********************************

# n=int(input('enter the number:'))
# for i in range(1,n):
#    print(i,end=' ')
#    sum=i*(i+1)//2
# print('and their sum is:',sum)

#**********************************

# dict1={
#         '1':{
#         'name':'khal drago',
#         'department':'Marketing',''
#         'Salary':50000,},

#         '2':{
#         'name':'Robb',
#         'department':'sales',
#         'Salary':50000,
#         },
       
      
#         '3':{
#         'name':'cersie',
#         'department':'business',
#         'Salary':50000,
#         },
       

#         '4':{
#         'name':'joffery',
#         'department':'hr',
#         'Salary':50000,
#         }, 
        
#         '5':{
#         'name':'sansa',
#         'department':'web dev',
#         'Salary':50000,
#     }
# }    
# print(dict1)

#**********************************

# a=int(input('enter the num:'))
# sum=0
# for i in range (1,a+1):
#    sum+=i
# print(sum)

#**********************************
# n=6
# for i in range(0,n):
#     for j in range(0,i+1):
#        print('*',end='')
#     print()


#**********************************



#**********************************
# n=int(input('enter a number:'))

# for i in range (n+1):
#     if i%2==0:
#      print(i)


#**********************************

# l=[1,2,3,45,67,25,25,74,25,20]  

# print('this is lenth',len(l))  
# if 25 in l:
#     print('present:',True)
# else:
#     print('present:',False)

# print('repeatation of number:',l.count(25))

# print('reversed:',l[10::-1])
# for i in l:
#     if i%2==0:
#      print('evens:',i)

#**********************************

# str1=input('enter the string:')
# print(str1)
# print(len(str1))

# if str1==str1[::-1]:
#     print('it is palindrome')
# else:
#     print('not palindrome')

# words=str1.split()
# print(words[len(words)//2])
# print(words[-2])


# X = ['abc', 'xyz', 'aba', '1221']

# count = 0

# for s in X:
#     if len(s) >= 2 and s[0] == s[-1]:
#         count += 1

# print(count)
