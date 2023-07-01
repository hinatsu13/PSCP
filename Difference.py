'''Difference'''
def main():
    '''Difference'''
    member_a = int(input())
    member_b = int(input())
    set_a = set()
    set_b = set()
    for _ in range(member_a):
        aaa = int(input())
        set_a.add(aaa)
    for _ in range(member_b):
        bbb = int(input())
        set_b.add(bbb)
    ans = sorted(set_a - set_b)
    print(*ans)
main()
