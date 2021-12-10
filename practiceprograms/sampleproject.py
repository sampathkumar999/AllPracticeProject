import random
def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    guess_count = 0
    limit = 3
    while guess_count < limit:
        guess = int(input(f'guess the no. netween 1 and {x}: '))
        guess_count += 1
        if guess == random_number:
            print('Great, you guessed the number!')
            break
        elif guess < random_number:
            print('sorry. Guess again. Too low')
        elif guess > random_number:
            print('sorry. Guess again. Too high')

    else:
        print('sorry you lost!')


guess(10)
        






