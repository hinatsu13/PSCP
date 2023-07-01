'''FibonacciRecursionV2'''
def fibo(number, fibona):
    '''find fibonacci srt'''
    start = len(fibona)
    if number in fibona:
        return
    
    fibo(number, fibona)

def main():
    '''FibonacciRecursionV2'''
    number = int(input())
    fibona = {0:0, 1:1}
    if number in fibona:
        print(fibona[number])
    else:
        fibo(number, fibona)
        print(fibona[number])
main()
