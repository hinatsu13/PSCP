'''AlmostMean'''
def main():
    '''AlmostMean'''
    student = int(input())
    paper1 = []
    paper2 = []
    for _ in range(student):
        score = input()
        paper1.append(score)
        score = score.split()
        paper2.append(float(score[1]))
    meann = sum(paper2) / student
    ans = max([i for i in paper2 if i <= meann])
    # เปรียบหาตัวที่มากที่สุดที่น้อยเท่ากับเท่ากับmean
    print(paper1[paper2.index(ans)])
main()
