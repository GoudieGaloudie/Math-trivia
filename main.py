import random

while True:
    print(r"""
+-------------------------------+
|          MATH TRIVIA          |
+-------------------------------+
|  1. Start game                |
|  2. Instructions              |
|  3. Quit                      |
+-------------------------------+
""")
    menu_choice = input("Choose an option: ").strip()

    if menu_choice == "1":
        break
    elif menu_choice == "2":
        print(
            "\nAnswer the math questions to earn points. "
            "You have 3 lives, and every 5th round is a boss round.\n"
            "Enter STOP, DONE, SCORE, OVER, or NO MORE to end the game.\n"
            "Choose a lower and upper number bound when the game starts.\n"
        )
        input("Press Enter to return to the menu...")
    elif menu_choice == "3":
        print("Goodbye!")
        raise SystemExit
    else:
        print("Please choose 1, 2, or 3.\n")

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

    try:  
        lower_bound = int(lower_input)
        upper_bound = int(upper_input)
        if upper_bound < lower_bound:
            continue
    except:
        print("Error, input valid upper and lower bounds")
        continue
    break

if lower_bound < 1 or upper_bound < 10:
    lower_bound = 1000
    upper_bound = 1001

operations = ['+', '*', '-', '/']
affirmations = ['Nice work', 'Keep it up!', 'Noice', 'You can do it!', 'Excellent!', 'You must be Einstein!']
bosswins = ['YOO NOICE JOB', 'DANG BRO NICE', '👍👍👍👍👍']
stop_words= ['STOP', 'DONE', 'SCORE', 'OVER', 'NO MORE']
allowed_set = {"0","1","2","3","4","5","6","7","8","9","+","-","/","*","(",")"}

# Main loop
while True:
    if secret == True:
        if round % 5 == 0:   
            a = random.randint(100, 100*upper_bound)
            b = random.randint(100, 100*upper_bound)

            question = str(a) + '*' + str(b)
            answer = input('BE EXTRA CAREFUL THIS IS THE BOSS ROUND' + ' WHAT IS ' + question + "?!?!?!? ")

            if set(answer) not in allowed_set:
                print("Please only enter valid answers!")
                continue

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

            
            if set(answer) not in allowed_set:
                print("Please only enter valid answers!")
                continue

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
        else:
            a = random.randint(lower_bound, upper_bound)
            b = random.randint(lower_bound, upper_bound)
            operator = random.choice(operations)

            question = str(a) + operator + str(b)
            answer = input('what is ' + question + "? ")

            if answer.upper() in stop_words:
                break

            if int(answer) == int(eval(question)):
                print(random.choice(affirmations))
                score += 1
                round += 1
            else:
                lifes -= 1
                round += 1
                print('You lost a life! You have ' + str(lifes) + ' lifes left.')
                if lifes == 0:
                    break
if score < 27:
    print('HA u lost to my first try XD but you did get ' + str(score) + ' points')
else:
    print('good job you beat me! you got ' + str(score) + ' points')