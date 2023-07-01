'''Meteorite'''
def main():
    '''Meteorite'''
    meteor = float(input())
    pice = int(input())
    safe = float(input())
    roundd = 0
    ans = 0
    picee = meteor / pice
    if meteor < safe:
        print('0')
    else:
        while True:
            roundd += pice ** ans
            if picee < safe:
                break
            ans += 1
            picee = picee / pice
        print(roundd)
main()
