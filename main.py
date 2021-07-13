print(logo)


def add(num1, num2):
    return num1+num2


def sub(num1, num2):
    return num1 - num2


def mul(num1, num2):
    return num1*num2


def div(num1, num2):
    return num1/num2


operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}


def calculator():
    flag = 'n'
    while flag == 'n':
        total = 0
        n1 = float(input("What's the first number: "))
        n2 = float(input("What's the second number: "))
        print('''
        +
        -
        *
        /
        ''')
        op = input("Pick an operation: ")
        calc = operations[op]
        total = calc(n1, n2)
        print(f"{n1} {op} {n2} = {total}")
        flag = input(f"Type 'y' to continue with {total}, or type 'n' to start a new calculation or 'e' to exit:\n").lower()
        if flag == 'e':
            exit(0)
        while flag == 'y':
            t = total
            n = float(input("What's the number: "))
            op = input("Pick an operation: ")
            calc = operations[op]
            total1 = calc(total, n)
            print(f"{t} {op} {n} = {total1}")
            flag = input(
                f"Type 'y' to continue with {total1}, or type 'n' to start a new calculation or 'e' to exit:\n").lower()
            if flag == 'e':
                exit(0)
                
                
calculator()
