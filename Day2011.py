'''Day2011'''
def main():
    '''Day2011'''
    day = int(input()) % 7
    monthh = int(input())
    if monthh == 1 or monthh == 10:
        saturdayy = {1:'Saturday', 2:'Sunday', 3:'Monday', 4:'Tuesday', 5:'Wednesday', \
        6:'Thursday', 0:'Friday'}
        print(saturdayy[day])
    elif monthh == 2 or monthh == 3 or monthh == 11:
        tuesdayy = {1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', \
        6:'Sunday', 0:'Monday'}
        print(tuesdayy[day])
    elif monthh == 4 or monthh == 7:
        fridayy = {1:'Friday', 2:'Saturday', 3:'Sunday', 4:'Monday', 5:'Tuesday', \
        6:'Wednesday', 0:'Thursday'}
        print(fridayy[day])
    elif monthh == 5:
        sundayy = {1:'Sunday', 2:'Monday', 3:'Tuesday', 4:'Wednesday', 5:'Thursday', \
        6:'Friday', 0:'Saturday'}
        print(sundayy[day])
    elif monthh == 6:
        wednesdayy = {1:'Wednesday', 2:'Thursday', 3:'Friday', 4:'Saturday', 5:'Sunday', \
        6:'Monday', 0:'Tuesday'}
        print(wednesdayy[day])
    elif monthh == 8:
        mondayy = {1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday', 5:'Friday', \
        6:'Saturday', 0:'Sunday'}
        print(mondayy[day])
    else:
        thurdayy = {1:'Thursday', 2:'Friday', 3:'Saturday', 4:'Sunday', 5:'Monday', \
        6:'Tuesday', 0:'Wednesday'}
        print(thurdayy[day])
main()






