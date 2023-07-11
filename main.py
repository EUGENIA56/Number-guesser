# importing random module
import random

# correct guess number
guess_number = 9
user_input = int(input('Enter guess a number(1-20): '))
if user_input == guess_number:
    print('You guess correct')
else:
    print('Guess is wrong')

# abc = random.randint(1, 10)
# print(abc)