'''Kaprekar'''
def main():
    '''Kaprekar'''
    number = input()
    number = "%04d" % int(number)
    count = 0
    while number != "6174":
        high = highnum(number)
        low = high[-1::-1]
        newnum = int(high) - int(low)
        count += 1
        number = "%04d" % (newnum)
    print(count)


def highnum(number):
    '''make highest number possible'''
    lst = [int(i) for i in number]
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] < lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    paper = ''
    for i in lst:
        paper += str(i)
    return paper
main()
