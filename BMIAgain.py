'''BMIAgain'''
def main():
    '''BMIAgain'''
    weight = int(input())
    high = int(input()) / 100
    bmi = weight / (high ** 2)
    if bmi >= 30:
        print('Obese')
    elif bmi >= 25 and bmi < 30:
        print('Overweight')
    elif bmi >= 18.5 and bmi < 25:
        print('Normal')
    elif bmi < 18.5:
        print('Underweight')
main()
