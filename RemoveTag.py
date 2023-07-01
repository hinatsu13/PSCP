'''RemoveTag'''
import re
def cleanhtml(raw_html):
    '''remove tag'''
    clean = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
    cleantext = re.sub(clean, ' ', raw_html)
    return cleantext

def main():
    '''RemoveTag'''
    raw_html = input()
    print(cleanhtml(raw_html).split())
main()
