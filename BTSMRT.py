'''BTSMRT'''
def main():
    '''BTSMRT'''
    day = input()
    age = float(input())
    high = float(input())
    if age < 14 and high < 90:
        print('FREE')
    elif day == 'Children Day' and age < 14 and high <= 140:
        print('FREE')
    elif day == "Senior Day" and age >= 60:
        print("FREE")
    else:
        print('PAY')
main()
