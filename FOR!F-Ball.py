'''FOR!F-Ball'''
def main():
    '''FOR!F-Ball'''
    ball = input()
    glass1 = 'ball'
    glass2 = 'none'
    glass3 = 'none'
    for i in ball:
        if i == 'A':
            glass1, glass2 = glass2, glass1
        elif i == 'B':
            glass2, glass3 = glass3, glass2
        else:
            glass1, glass3 = glass3, glass1
    if glass1 == 'ball':
        print('1')
    elif glass2 == 'ball':
        print('2')
    else:
        print('3')
main()
