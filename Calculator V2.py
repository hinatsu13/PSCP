'''Calculator V2'''
def main():
    '''Calculator V2'''
    number = int(input())
    paper = 0
    if number == 1:
        print('1')
        return # มีเพื่อนไม่ให้คืนค่ามากกว่า 1 ค่า
    elif len(str(number)) == 1:
        paper += number
    else:
        for i in range(len(str(number))):
            if i == 0:
                paper += (number - 10 ** (len(str(number)) - 1) + 1) * len(str(number))
            else:
                paper += (9 * (10 ** (len(str(number)) - i - 1))) * (len(str(number)) - i)
    print(paper + number)
main()
