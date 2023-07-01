'''Classify'''
def main():
    '''Classify'''
    paper = []
    all_year = []
    while True:
        student_id = input()
        if student_id == 'END':
            break
        all_year.append(int(student_id[:2]))
        paper.append(student_id)
    allyear = sorted(list(dict.fromkeys(all_year)))
    for current_year in allyear:
        faculty = []
        for j in paper:
            if int(j[:2]) == current_year:
                faculty.append(int(j[2:4]))
        faculty_nodup = dict.fromkeys(sorted(faculty))
        for i in faculty_nodup:
            temp = 0
            for j in paper:
                if int(j[:2]) == current_year and int(j[2:4]) == i:
                    temp += 1
            faculty_nodup[i] = temp
        cheakk = False
        for key, values in faculty_nodup.items():
            if cheakk:
                print('--', end=' ')
            else:
                print(current_year, end=' ')
                cheakk = True
            print(key, values)
main()
