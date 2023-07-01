'''RectangleArea'''
def main():
    '''RectangleArea'''
    pic_a = list(map(int, input().split()))
    pic_b = list(map(int, input().split()))
    legnth_x_a = pic_a[0] + pic_a[2]
    legnth_y_a = pic_a[1] + pic_a[3]
    legnth_x_b = pic_b[0] + pic_b[2]
    legnth_y_b = pic_b[1] + pic_b[3]
    area_x = max(0, min(legnth_x_a, legnth_x_b) - max(pic_a[0], pic_b[0]))
    area_y = max(0, min(legnth_y_a, legnth_y_b) - max(pic_a[1], pic_b[1]))
    # หาความยาวของแต่ละด้าน
    ans = area_x * area_y
    if ans == 0:
        print('no overlapping')
    else:
        print(ans)
main()
