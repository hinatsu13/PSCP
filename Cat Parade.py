'''Cat Parade'''
def main():
    '''Cat Parade'''
    paper = [] #listเปล่า
    while True:
        text = input()
        if text == 'END':
            break #ถ้าเจอ end หยุด
        elif text == 'IT\'S A DOG':
            paper.remove(paper[len(paper)-1]) #remvoe ตัวก่อนเพราะใส่ผิด
        else:
            text = text.split(', ')
            for i in text:
                paper.append(i)
    paper2 = paper.copy() #ก๊อปlist
    paper2.sort()
    for i in paper2:
        if paper2.count(i) > 1:
            while paper2.count(i) > 1:
                paper2.remove(i)
    for i in paper2:
        print('%s %d %d' %(i, paper.index(i) + 1, paper.count(i)))
main()
