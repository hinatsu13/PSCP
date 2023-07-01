'''RunGame'''
def main():
    '''RunGame'''
    runing = list(map(int, input().split()))
    lenght = 0
    for i in range(len(runing)):
        if i == 0:
            lenght += abs(runing[0])
        else:
            lenght += abs(runing[i -1] - runing[i])
    print(lenght)
main()
