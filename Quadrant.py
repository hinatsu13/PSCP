'''Quadrant'''
def main():
    '''Quadrant'''
    numx = int(input())
    numy = int(input())
    if numx > 0 and numy > 0:
        print('Q1')
    elif numx < 0 and numy > 0:
        print('Q2')
    elif numx < 0 and numy < 0:
        print('Q3')
    elif numx > 0 and numy < 0:
        print('Q4')
    elif numx == 0 and numy > 0 or numy < 0:
        print('Y')
    elif numy == 0 and numx > 0 or numx < 0:
        print('X')
    elif numx == 0 and numy == 0:
        print('O')
main()
