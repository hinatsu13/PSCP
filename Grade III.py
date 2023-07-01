'''Grade III'''
def main():
    '''Grade III'''
    subject = int(input())
    summ = 0
    for _ in range(subject):
        score = float(input())
        if score >= 95:
            summ += 4
        elif score >= 90:
            summ += 3.5
        elif score >= 85:
            summ += 3
        elif score >= 80:
            summ += 2.5
        elif score >= 75:
            summ += 2
        elif score >= 70:
            summ += 1.5
        elif score >= 65:
            summ += 1
        elif score >= 60:
            summ += 0.5
        else:
            summ += 0
    print('%.2f' %((int(summ * 100 / subject) / 100)))
main()
