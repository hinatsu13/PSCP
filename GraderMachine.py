'''GraderMachine'''
def main():
    '''GraderMachine'''
    start = int(input())
    stop = int(input())
    ans = 0
    paper = ""
    if start < stop:
        for i in range(start, stop + 1):
            if i % 2 == 0:
                ans += i
                paper = paper + str(i) + ' '
            else:
                pass
        print('pass : ' + paper + "\nSum : %d" %ans)
    elif start > stop:
        for i in range(start, stop - 1, -1):
            if i % 2 == 0:
                ans += i
                paper = paper + str(i) + ' '
            else:
                pass
        print('pass : ' + paper + "\nSum : %d" %ans)
    elif start == stop:
        print('pass : %d' %start + "\nSum : %d" %start)
main()
