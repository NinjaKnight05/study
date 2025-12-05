# data={'movie':'anurag','year':4564}



# if len(data)==0:
#     print('no movies')
# else:
#    s=input('movie type:')
#    for i,j in enumerate(data):
#      if s in  (j['movie']):
#         print('done')
#      else:
#         print('sorry')


# n=100
# if n%2!=0:
#     print('Weird')
# elif n%2==0 and n>=2 and n<=5:
#     print('Not Weird')
# elif n%2==0 and n>=6 and n<=20:
#     print('Weird')
# elif n%2==0 and n>20:
#     print('Not Weird')

# def is_leap(year):
#     leap = False
    
#     # Write your logic here
#     if year%4==0:
#      leap=True
#     elif year%400==0:
#       leap=True
#     elif year%100==0:
#       leap=False
#     else:
#       leap=False
    
#     return leap



# year=2500
# if year%4==0 and year%400==0:
#   print('its leap year')
# else:
#   print('not leap year')

# if __name__ == '__main__':
#     n = int(input('enter n:'))
#     for i in range(n):
#         print(i+1,end='')
# _a10=10
# b=10
# b[10]=2
# print(b)
# a=-2.0
# print(a)

# my_list = ['hello', ' world']
# my_bae=' hiii'
# joined_my_str = my_bae.join(my_list)
# print(joined_my_str) 
# print(my_list)

# a=30
# a-=10
# print(a)

is_citizen = True
age = 11

if is_citizen and age >= 18:
    print('You are eligible to vote') # You are eligible to vote
else:
    print('You are not eligible to vote')