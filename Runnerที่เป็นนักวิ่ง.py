'''Runnerที่เป็นนักวิ่ง'''
def main():
    '''Runnerที่เป็นนักวิ่ง'''
    distances = int(input())
    how_many_runner = int(input())
    paper = []
    for _ in range(how_many_runner):
        runner = [int(x) for x in input().split()]
        runner[1] = distances - runner[1]
        runner[1] = runner[1] / runner[0]
        paper.append(runner)
    for i in range(len(paper)):
        if i == 0:
            fastest = paper[0]
        if fastest[1] > paper[i][1]:
            fastest = paper[i]
        if fastest[1] == paper[i][1]:
            if fastest[0] > paper[i][0]:
                fastest = fastest
            else:
                fastest = paper[i]
    print(paper.index(fastest) + 1)
main()
