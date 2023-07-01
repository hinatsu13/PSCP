'''temperature'''
def tem(temperature, unit_start, unit_want):
    '''find unit you want'''
    celsi = 0
    if unit_start == 'F':
        celsi += (temperature - 32) * (5 / 9)
    elif unit_start == 'R':
        celsi += (temperature - 491.67) * (5 / 9)
    elif unit_start == 'K':
        celsi += temperature - 273.15
    else:
        celsi += temperature
    if unit_want == 'F':
        return '%.2f' %((celsi * (9 / 5)) +32)
    elif unit_want == 'K':
        return '%.2f' %(celsi + 273.15)
    elif unit_want == 'R':
        return '%.2f' %((celsi + 273.15) * (9 / 5))
    else:
        return '%.2f' %celsi

def main():
    '''temperature'''
    temperature = float(input())
    unit_start = input()
    unit_want = input()
    if unit_start == unit_want:
        print('%.2f' %temperature)
    else:
        print(tem(temperature, unit_start, unit_want))
main()
