'''ClockHands'''
def main():
    '''ClockHands'''
    hour = int(input())
    minise = int(input())
    hour *= 5
    hour += minise / 12 # 12 องศาของนาที = 1องศาของชั่วโมง?
    hour %= 60 # น่าจะเอานาทีมาละมั้ง แบะๆ
    print(minise <= hour < minise + 1)
main()
