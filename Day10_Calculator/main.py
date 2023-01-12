from Day11_The_Blackjack.logo import logo

def add(num1, num2):
    """將兩個數字相加

    Args:
        num1 (float) : 第一個輸入的數字

        num2 (float) : 第二個輸入的數字

    Yields:
        result (float) : 相加後的數字

    """
    return num1 + num2

def reduce(num1, num2):
    """將兩個數字相減

    Args:
        num1 (float) : 第一個輸入的數字

        num2 (float) : 第二個輸入的數字

    Yields:
        result (float) : 相減後的數字

    """
    return num1 - num2

def multiplied(num1, num2):
    """將兩個數字相乘

    Args:
        num1 (float) : 第一個輸入的數字

        num2 (float) : 第二個輸入的數字

    Yields:
        result (float) : 相乘後的數字

    """
    return num1 * num2

def divide(num1, num2):
    """將兩個數字相除

    Args:
        num1 (float) : 第一個輸入的數字

        num2 (float) : 第二個輸入的數字

    Yields:
        result (float) : 相除後的數字

    """
    return num1 / num2

def Calculator():
    print (logo)
    result = 0
    keep_going = True

    num1 = float(input("Input the first number: "))
    operators = {
    "+" : add,
    "-" : reduce,
    "*" : multiplied,
    "/" : divide
    }

    while keep_going:

        for key in operators:
            print(key)
        action = input("Which operator do you choose: ")
        operator_function = operators[action]

        num2 = float(input("Input the number you want to act on the previous num: "))
        result = operator_function(num1, num2)
        print(f"The result is {result}")
        num1 = result
        keep = input("Type 'keep' to continue with the result or 'new' to create a new calculator or 'end' to end this program: ")
        if keep == "keep":
            continue
        elif keep == "end":
            keep_going = False
            break
        elif keep == "new":
            Calculator()
        else :
            print("Wrong input! End the program!")
            keep_going = False
            break

Calculator()