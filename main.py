import random

score = 0
lifes = 3
round = 1
secret = False

SECRET_CODE = '123abc!@#ABC'

while True:
    lower_input = input('Lower bound for number for equation: ')
    if lower_input == SECRET_CODE:
        secret = True
        continue

    upper_input = input('Upper bound for number for equation: ')
    if upper_input == SECRET_CODE:
        secret = True
        continue

    lower_bound = int(lower_input)
    upper_bound = int(upper_input)
    break

if lower_bound < 1 or upper_bound < 10:
    lower_bound = 1000
    upper_bound = 1001

operations = ['+', '*', '-', '/']
affirmations = ['Nice work', 'Keep it up!', 'Noice', 'You can do it!']
bosswins = ['YOO NOICE JOB', 'DANG BRO NICE', '👍👍👍👍👍']
stop_words= ['STOP', 'DONE', 'SCORE', 'OVER', 'NO MORE']

# Main loop
while True:
    if secret == True:
        if round % 5 == 0:   
            a = random.randint(100, 100*upper_bound)
            b = random.randint(100, 100*upper_bound)

            question = str(a) + '*' + str(b)
            answer = input('BE EXTRA CAREFUL THIS IS THE BOSS ROUND' + ' WHAT IS ' + question + "?!?!?!? ")

            # Life system
            if int(eval(answer)) == int(eval(question)):
                print(random.choice(bosswins))
                score += 5
                round += 1
            else:
                print('You lost to the boss!')
                break
        else:
            a = random.randint(lower_bound, upper_bound)
            b = random.randint(lower_bound, upper_bound)

            operator = random.choice(operations)

            question = str(a) + operator + str(b)
            answer = input('what is ' + question + "? ")

            # Checks if its a stop word if so it stops
            if answer.upper() in stop_words:
                break

            # Life system
            if int(eval(answer)) == int(eval(question)):
                print(random.choice(affirmations))
                score += 1
                round +=1
            else:
                lifes -= 1
                round += 1
                print('You lost a life! You have ' + str(lifes) + ' lifes left.')
                if lifes == 0:
                    break
    else:
        if round % 5 == 0:   
                a = random.randint(100, 100*upper_bound)
                b = random.randint(100, 100*upper_bound)
        
                question = str(a) + '*' + str(b)
                answer = input('BE EXTRA CAREFUL THIS IS THE BOSS ROUND' + ' WHAT IS ' + question + "?!?!?!? ")
        
                # Life system
                if int(answer) == int(eval(question)):
                    print(random.choice(bosswins))
                    score += 5
                    round += 1
                else:
                    print('You lost to the boss!')
                    break    
if score < 27:
    print('HA u lost to my first try XD but you did get ' + str(score) + ' points')
else:
    print('good job you beat me! you got ' + str(score) + ' points')