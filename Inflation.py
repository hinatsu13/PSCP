'''Inflation'''
def main():
    '''Inflation'''
    value = float(input())
    year = int(input())
    value = int(value * 100)
    for _ in range(year):
        digit = value * 381
        value = value + digit // 10000
    digit = str(value)[-2:]
    value = str(value)[:-2]
    if value == "":
        value = "0"
    print("%d.%02d" %(int(value), int(digit)))
main()
