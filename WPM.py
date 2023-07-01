'''WPM'''
def kid(speed):
    '''find from kid'''
    if speed < 11:
        return 'Very Slow'
    elif speed < 21:
        return 'Slow'
    elif speed < 31:
        return 'Average'
    elif speed < 41:
        return 'Fast'
    elif speed > 40:
        return 'Very Fast'

def main():
    '''WPM'''
    age = input()
    speed = int(input())
    if age == 'Kids':
        print(kid(speed))
    elif age == 'Adults':
        if speed < 26:
            print('Very Slow')
        elif speed < 36:
            print('Slow/Beginner')
        elif speed < 46:
            print('Intermediate/Average')
        elif speed < 66:
            print('Fast/Advanced')
        elif speed < 81:
            print('Very Fast')
        elif speed > 80:
            print('Insane')
main()
