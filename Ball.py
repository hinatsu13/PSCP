'''Ball'''
def main():
    '''Ball'''
    high = float(input())
    roundd = 0
    while high > 0.01: # เช็คว่าความสูงมากกว่า 1 ซม.ไหม ถ้าน้อยกว่าloopจะหยุด
        high = high * (3 / 5)
        roundd += 1
    if roundd > 0:
        print(roundd - 1)
    else:
        print('0')
main()
