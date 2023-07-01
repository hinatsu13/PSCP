'''WeightStation'''
def main():
    '''WeightStation'''
    value = float(input())
    wheel1 = float(input())
    wheel2 = float(input())
    wheel3 = float(input())
    wheel4 = (value * 4) - (wheel1 + wheel2 + wheel3)
    val2 = value / 2
    if value * 4 > 15000:
        print('Overweight')
    else:
        if abs(wheel1 - value) <= val2 and abs(wheel2 - value) <= val2 and abs(wheel3 - value)\
        <= val2 and abs(wheel4 - value) <= val2:
            print('Pass %.2f' %(wheel4))
        else:
            print('Unbalance')
main()
