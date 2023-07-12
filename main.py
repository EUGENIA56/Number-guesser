# importing random module
import random

# correct guess number

i=0
number_of_chances=0
while i<5:
    guess_number = random.randint(1, 20)
    user_input = int(input('Enter guess a number(1-20): '))
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

abc = random.randint(1, 10)
print(abc)

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