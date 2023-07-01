'''NumDays'''
def main(start_day, start_month, end_day, end_month):
    '''NumDays'''
    count_day = 0
    month = {'1':31, '2':28, '3':31, '4':30, '5':31, '6':30, '7':31, '8':31, '9':30, \
    '10':31, '11':30, '12':31}
    if start_day > month[start_month] or end_day > month[end_month]:
        print('Impossible')
    elif start_month == end_month:
        print(abs(start_day - end_day))
    else:
        for i in range(abs(int(end_month) - int(start_month))):
            if i == 0:
                count_day += month[start_month] - start_day
                monthh = str(int(start_month) + 1)
            if i == abs(int(end_month) - int(start_month)) - 1:
                count_day += end_day
            else:
                count_day += month[monthh]
                monthh = str(int(monthh) + 1)
        print(count_day)
main(int(input()), input(), int(input()), input())
