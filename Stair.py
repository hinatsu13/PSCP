'''Stair'''
def main():
    '''Stair'''
    highest = int(input())
    step = int(input())
    count = 0
    check = 0
    overflow = True
    for _ in range(step):
        height = int(input())
        check += height
        if height > highest:
            overflow = False
        elif check == highest:
            count += 1
            check = 0
        elif check > highest:
            count += 1
            check = height
    if check > 0:
        count += 1
    if overflow == True:
        print(count)
    else:
        print("NO")
main()
