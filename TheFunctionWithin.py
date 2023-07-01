'''TheFunctionWithin'''
def main(num_a, num_b, num_c, num_d):
    '''TheFunctionWithin'''
    print(num_a * 2 * 2)
    ans_f = 2 * (num_a - num_b)
    print((3 * (ans_f  ** 4)) - (ans_f ** 3) + (2 * (ans_f ** 2)) + 10)
    ans_x = 2 * (num_a + num_b)
    ans_y = 2 * (num_a + num_c)
    ans_z2 = (3 * ((2 * (num_d ** 2))  ** 4)) - \
    ((2 * (num_d ** 2)) ** 3) + (2 * ((2 * (num_d ** 2)) ** 2)) + 10
    print(((ans_z2 + ans_x) ** 2) - (ans_x * ans_y) + (ans_y ** 2))
    ans1 = 2 * (num_a + num_b)
    ans2 = 2 * (num_a - num_c)
    ans3 = 2 * (num_d ** 2)
    ans4 = (3 * (ans3  ** 4)) - (ans3 ** 3) + (2 * (ans3 ** 2)) + 10
    ans_a = ((ans4 + ans1) ** 2) - (ans1 * ans2) + (ans2 ** 2)
    ans5 = 2 * (num_a - num_b)
    ans_b = (3 * (ans5  ** 4)) - (ans5 ** 3) + (2 * (ans5 ** 2)) + 10
    print((ans_a ** 2 + ans_b ** 2 - (num_c * 32) ** 2) \
          / (((num_d ** 8) ** 2) - (2 * ans_a * (num_d ** 8)) + 2 * ans_a))
main(float(input()), float(input()), float(input()), float(input()))
