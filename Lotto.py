'''Lotto'''
def main():
    '''Lotto'''
    prize_1 = input()
    prize_last2 = input()
    prize_first3_1 = input()
    prize_first3_2 = input()
    prize_last3_1 = input()
    prize_last3_2 = input()
    my_lotto = input()
    money = 0
    if prize_1 == '000000':
        prize_2_1 = '000001'
        prize_2_2 = '999999'
    elif prize_1 == '999999':
        prize_2_1 = '000000'
        prize_2_2 = '999998'
    else:
        prize_2_1 = '%06d' %(int(prize_1) + 1)
        prize_2_2 = '%06d' %(int(prize_1) - 1)
    if my_lotto == prize_1:
        money += 6000000
    if my_lotto[-2:] == prize_last2:
        money += 2000
    if my_lotto[:3] == prize_first3_1:
        money += 4000
    if my_lotto[:3] == prize_first3_2:
        money += 4000
    if my_lotto[-3:] == prize_last3_1:
        money += 4000
    if my_lotto[-3:] == prize_last3_2:
        money += 4000
    if my_lotto == prize_2_1 or my_lotto == prize_2_2:
        money += 100000
    print(money)
main()
