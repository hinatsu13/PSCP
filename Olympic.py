'''Olympic'''
def main():
    '''Olympic'''
    many_country = int(input())
    data = []
    for _ in range(many_country):
        country = input().split()
        country_list = [list(map(int, country[1:])), sum(list(map(int, country[1:]))), country[0]]
        # เป็น list ที่เก็บทีมแต่ละประเทศกับจำนวนเหรียญทองที่ได้แยกออกจากกัน
        data.append(country_list)
    data.sort(reverse=True)
    roundd = 1
    lis = []
    tmp2, tmp3 = [], 0 #tmp2 คือ อันดับที่ควรจะอยู่, tmp3 คือเก็บตำแหน่งเดียวกัน
    for i in range(len(data)):
        tmp = []
        if data[i][0] == tmp2:
            tmp.append(tmp3)
        else:
            tmp.append(roundd)
            tmp3 = roundd
        tmp.append(data[i][2])
        for j in data[i][0]:
            tmp.append(j)
        tmp.append(data[i][1])
        roundd += 1
        tmp2 = data[i][0]
        lis.append(tmp)
    lis.sort()
    for i in lis:
        print(*i)
main()
