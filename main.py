import ast
import random
from fractions import Fraction

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


def arithmetic_value(expression):
    if len(expression) > 200:
        raise ValueError('Expression is too long')

    tree = ast.parse(expression, mode='eval')
    if sum(1 for _ in ast.walk(tree)) > 100:
        raise ValueError('Expression is too complex')

    def calculate(node):
        if isinstance(node, ast.Expression):
            return calculate(node.body)
        if isinstance(node, ast.Constant) and type(node.value) is int:
            return Fraction(node.value)
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
            value = calculate(node.operand)
            return value if isinstance(node.op, ast.UAdd) else -value
        if isinstance(node, ast.BinOp):
            left = calculate(node.left)
            right = calculate(node.right)
            if isinstance(node.op, ast.Add):
                return left + right
            if isinstance(node.op, ast.Sub):
                return left - right
            if isinstance(node.op, ast.Mult):
                return left * right
            if isinstance(node.op, ast.Div):
                return left / right
        raise ValueError('Only basic arithmetic is allowed')

    return calculate(tree)


def answer_is_correct(answer, question, allow_expressions):
    try:
        answer_value = arithmetic_value(answer) if allow_expressions else Fraction(int(answer))
        return int(answer_value) == int(arithmetic_value(question))
    except (SyntaxError, ValueError, TypeError, ZeroDivisionError, RecursionError):
        return False


# Main loop
while True:
    if secret == True:
        if round % 5 == 0:   
            a = random.randint(100, 100*upper_bound)
            b = random.randint(100, 100*upper_bound)

            question = str(a) + '*' + str(b)
            answer = input('BE EXTRA CAREFUL THIS IS THE BOSS ROUND' + ' WHAT IS ' + question + "?!?!?!? ")

            # Life system
            if answer_is_correct(answer, question, allow_expressions=True):
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
            if answer_is_correct(answer, question, allow_expressions=True):
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
                if answer_is_correct(answer, question, allow_expressions=False):
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