# #--------------question 1-------------------
# str='coder roots';
# print(str[0:2],end='');
# print(str[9:11]);
# str2='new year';
# print(str2[0:2],end='');
# print(str2[6:8]);


# #----------------question 1 with user values---------

# str=input('enter the first word:')
# str2=input('enter the secand word:')

# n1=int(input('enter the start index value of first word(0-n):'));
# n2=int(input('enter the end index value of first word(1-n):'));

# n3=int(input('enter the start index value of secand word(0-n):'));
# n4=int(input('enter the end index value of secand word(1-n):'));

# print(str[n1:n2],end='');
# print(str2[n3:n4]);


# #----------------question 2 ------------------
# str='coder';
# str2='roots';
# print(str.replace('c','r'),end=' ')
# print(str2.replace('r','c'))

# #---------------questtion 3 -----------------

# str='abc';
# print(str.replace('c','cing'));
# str2='string';
# print(str2.replace('g','gly'))


# #-------------------question 3 with user input---------------------
# str=input('enter the string:')

# if 'ing'not in str:
#     print(str+'ing')
# elif 'ing' in str:
#     print(str+'ly')


# #--------------question  4-----------------

# str=input('enter the word:')
# n=int(input('enter the index value:'))
# print(str[:n]+str[n+1:])

