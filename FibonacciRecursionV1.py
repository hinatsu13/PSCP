'''FibonacciRecursionV1'''
def fun(number):
    """find something"""
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fun(number - 1) + fun(number - 2)

def main():
    """I hate Fibonacci"""
    num = int(input())
    print(fun(num))
main()
