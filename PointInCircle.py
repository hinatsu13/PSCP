'''PointInCircle''' 
def main():
    '''PointInCircle'''
    middle_x = float(input())
    middle_y = float(input())
    redius = float(input())
    point_x = float(input())
    point_y = float(input())
    ans = ((point_x - middle_x) ** 2 + (point_y - middle_y) ** 2) ** 0.5
    if ans <= redius:
        print('True')
    else:
        print('False')
main()
