# def get_sum(num_1, num_2):
#     return num_1 + num_2

# result = get_sum(3, 4) 


# def greet():
#     print('hello') 

# result = greet() # hello
# print(result) #


# def say_hello():
#     name = input('What is your name? ')
#     return 'Hello ' + name

# def uppercase_decorator(func):
#     def wrapper():
#         original_func = func()
#         modified_func = original_func.upper()
#         return modified_func
#     return wrapper

# say_hello_res = uppercase_decorator(say_hello)

# print(say_hello_res())



# arr=[1,2,3,4]
# arr.insert(0,5)
# print(arr)

# secret_number = 3
# guess = 0

# while guess != secret_number:
#     guess = int(input('Guess the number (1-5): '))
#     if guess != secret_number:
#         print('Wrong! Try again.')

# print('You got it!')

# developer_names = ['Jess', 'Naomi', 'Tom']

# for developer in developer_names:
#     if developer == 'Naomi':
#         break
#     print(developer)

# words = ['sky', 'apple', 'rhythm', 'fly', 'orange']

# for word in words:
#     for letter in word:
#         if 'aeiou' in letter.lower()  :
#             print(f"'{word}' contains the vowel '{letter}'")
#             break
#     else:
#         print(f"'{word}' has no vowels")

# developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
# ids = [1, 2, 3, 4]

# for name, id in zip(developers, ids):
#     print(f'Name: {name}')
#     print(f'ID: {id}')

numbers = [1, 2, 3, 4, 5]
result = [(num, 'Even') if num % 2 == 0 else (num, 'Odd') for num in numbers]
print(result)