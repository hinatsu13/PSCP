'''BloodDonation'''
def main():
    '''BloodDonation'''
    age = int(input())
    weight = int(input())
    donate = int(input())
    if age == 17 or (age >= 60 and age <= 70):
        letter = input()
        if weight < 45 or letter == 'False' or age > 70:
            print('No')
        elif donate == 0 and age >= 60:
            print('No')
        else:
            print('Yes')
    else:
        if weight < 45 or age < 17 or age > 70:
            print('No')
        elif donate == 0 and age > 55:
            print('No')
        else:
            print('Yes')
main()
