'''CuteCat CuteFox'''
import json
def main():
    '''CuteCat CuteFox'''
    many = int(input())
    both = {}
    cat = 0
    fox = 0
    for _ in range(many):
        idk = input()
        if "'" in idk:
            idk = idk.replace("'", '"')
        if '"' not in idk:
            idk = idk.replace("{", '{"').replace("}", '"}').replace(":", '" : "')
        if 'Cat' in idk:
            cat += 1
        else:
            fox += 1
        idk = json.loads(idk)
        both.update(idk)
    if 'Cat01' not in both.values() and 'Garfield' not in both.keys():
        cat += 1
        both['Garfield'] = 'Cat01'
    if 'Fox01' not in both.values() and 'Fubuki' not in both.keys():
        fox += 1
        both['Fubuki'] = 'Fox01'
    both = dict(sorted(both.items(), key=lambda x: x[1]))
    print('Cat :', cat)
    print('Fox :', fox)
    for key, value in both.items():
        print(key, ':', value)
main()
