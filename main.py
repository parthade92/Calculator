logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


print(logo)


def add(num1, num2):
    return num1+num2


def sub(num1, num2):
    return num1 - num2


def mul(num1, num2):
    return num1*num2


def div(num1, num2):
    return num1/num2


flag = 'n'
while flag == 'n':
    total = 0
    n1 = float(input("What's the first number: "))
    print('''
    +
    -
    *
    /
    ''')
    op = input("Pick an operation: ")
    n2 = float(input("What's the second number: "))
    if op == "+":
        total = add(n1, n2)
    elif op == "-":
        total = sub(n1, n2)
    elif op == "*":
        total = mul(n1, n2)
    elif op == "/":
        total = div(n1, n2)
    else:
        print("Invalid Input")
    print(f"{n1} {op} {n2} = {total}")
    flag = input(f"Type 'y' to continue with {total}, or type 'n' to start a new calculation or 'e' to exit:\n").lower()
    if flag == 'e':
        exit(0)
    while flag == 'y':
        t = total
        op = input("Pick an operation: ")
        n = float(input("What's the number: "))
        if op == "+":
            total = add(total, n)
        elif op == "-":
            total = sub(total, n)
        elif op == "*":
            total = mul(total, n)
        elif op == "/":
            total = div(total, n)
        else:
            print("Invalid Input")
        print(f"{t} {op} {n} = {total}")
        flag = input(
            f"Type 'y' to continue with {total}, or type 'n' to start a new calculation or 'e' to exit:\n").lower()
        if flag == 'e':
            exit(0)
