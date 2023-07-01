'''Stepper II'''
def main():
    '''Stepper II'''
    start = int(input())
    stop = int(input())
    if start <= stop:
        for i in range(start, stop + 1):
            print(i)
    elif start > stop:
        for i in range(start, stop - 1, -1):
            print(i)
main()
