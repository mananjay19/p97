import random
print('number guessing game')

number=random.randint(1,9)
print(number)
chances=0
print('guess a number between 1 to 9')
while chances<5:
    guess=int(input('enter the number you guessed: '))
    if guess==number:
        print('congratulations you WIN')
    elif guess<number:
        print('guess was low try guessing a higher number')
    else:
        print('your guess was too higher try guessing a bit lower')
    chances+=1
if not chances<5:
    print('you LOSE better luck next timethe number was: ',number)