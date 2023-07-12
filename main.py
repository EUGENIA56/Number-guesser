# importing random module
import random

# start game level instructions
user_level = input('****Choose level**** \n' 
                   '1.Beginner(1-20) \n'
                   '2. Intermmidiate(1-100) \n' 
                   '3. Hard(1-1000) \n\n'
                    'Provide level: ')
user_level = int(user_level)
level = 0
if user_level == 1:
    level = 20
elif user_level == 2:
    level = 100
elif user_level == 3:
    level = 1000
else:
    print('Invalid user input')
    exit(1)

# correct guess number

i=0
number_of_chances=0
while i<5:
    guess_number = random.randint(1, level)
    user_input = int(input(f'Enter guess a number(1-{level}): '))
    number_of_chances+=1
    if user_input == guess_number:
        print('You guess correct')
        res = 'You won and you used {} chances'
        print(res.format(number_of_chances))
        break
    else:
        print('Guess is wrong')
        if user_input > guess_number:
            print('Your number is too high, try again!!')
        else:
            print('Your guesss is too low, try again!!')
    i=i+1
print('Program ended, Thanks for guessing')

# abc = random.randint(1, 10)
# print(abc)

# break
# for i in range(10):
#     if i == 2:
#         break
#     print('Hello World')

# continue                                                                        
# for i in range(10):
#     if i == 2:
#         continue
#     print(i)