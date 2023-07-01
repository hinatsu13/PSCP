'''PrasomSib'''
def main():
    '''PrasomSib'''
    number = input()
    how_many = 0
    start, stop, plus = 0, 2, 0
    while True:
        if len(number) < stop + plus: # substringเกินขอบเขตของตัวnumber
            break
        temp = list(map(int, list(number[start:stop + plus])))
        if sum(temp) == 10:
            how_many += 1
            start += 1
            stop += 1
        if sum(temp) < 10:
            plus += 1
        if sum(temp) > 10:
            start += 1
            stop += 1
            plus = 0
    print(how_many)
main()
