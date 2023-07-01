'''Palindrome'''
def main():
    '''Palindrome'''
    many = int(input())
    time = input()
    count = 0
    while count != many:
        hour = time[:2].replace(":", "")
        mit = "%02d" %(int(time[-2:]) + 1)
        if int(mit) == 60:
            hour = str(int(hour) + 1)
            mit = "00"
        if hour == '24':
            hour = '0'
        time = hour + ":" + mit
        if time.replace(":", "") == time.replace(":", "")[::-1]:
            print(time)
            count += 1
main()
