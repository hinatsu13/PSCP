'''BreachTheDoor'''
def main():
    '''BreachTheDoor'''
    sentance = input().split()
    password = ''
    countt = 0
    for i in sentance:
        for j in i:
            if not j.isidentifier():
                i = i.replace(j, '')
            else:
                countt += 1
        if countt > 6:
            password += i + ' '
        else:
            pass
        countt = 0
    print(password)
main()
