'''BMI'''
def main():
    '''BMI 5 person'''
    name1 = input()
    weight1 = float(input())
    high1 = float(input()) / 100
    name2 = input()
    weight2 = float(input())
    high2 = float(input()) / 100
    name3 = input()
    weight3 = float(input())
    high3 = float(input()) / 100
    name4 = input()
    weight4 = float(input())
    high4 = float(input()) / 100
    name5 = input()
    weight5 = float(input())
    high5 = float(input()) / 100
    print(name1 + "'s  BMI = %.2f" %(weight1 / (high1 ** 2)))
    print(name2 + "'s  BMI = %.2f" %(weight2 / (high2 ** 2)))
    print(name3 + "'s  BMI = %.2f" %(weight3 / (high3 ** 2)))
    print(name4 + "'s  BMI = %.2f" %(weight4 / (high4 ** 2)))
    print(name5 + "'s  BMI = %.2f" %(weight5 / (high5 ** 2)))
main()
