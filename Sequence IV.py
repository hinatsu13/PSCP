'''Sequence IV'''
def main():
    '''Sequence IV'''
    num = int(input())
    for row in range(1, num + 1):
        rows = ((row - 1) * num) + 1 # เริ่มตัวใหม่ของทุกแถว
        for _ in range(num):
            print(rows, end=' ')
            rows += 1 # เอาตัวแรกมา +1 แล้ววนลูป
        print()
main()
