'''iPhone 13 Again'''
def mini(mem):
    """iPhone 13 mini"""
    if mem == '128 GB':
        return '25900'
    elif mem == '256 GB':
        return '29900'
    elif mem == '512 GB':
        return '37900'
    else:
        return 'Not Available'

def ip13(mem):
    """iPhone 13 """
    if mem == '128 GB':
        return '29900'
    elif mem == '256 GB':
        return '33900'
    elif mem == '512 GB':
        return '41900'
    else:
        return 'Not Available'

def pro(mem):
    '''iPhone 13 Pro'''
    if mem == '128 GB':
        return '38900'
    elif mem == '256 GB':
        return '42900'
    elif mem == '512 GB':
        return '50900'
    elif mem == '1 TB':
        return '58900'
    else:
        return 'Not Available'

def promax(mem):
    '''iPhone 13 Pro Max'''
    if mem == '128 GB':
        return '42900'
    elif mem == '256 GB':
        return '46900'
    elif mem == '512 GB':
        return '46900'
    elif mem == ('1 TB'):
        return '62900'
    else:
        return 'Not Available'

def main():
    """[Recommend] iPhone 13 Again"""
    ver = input()
    mem = input()
    if ver == 'iPhone 13 mini':
        print(mini(mem))
    elif ver == 'iPhone 13':
        print(ip13(mem))
    elif ver == 'iPhone 13 Pro':
        print(pro(mem))
    elif ver == 'iPhone 13 Pro Max':
        print(promax(mem))
    else:
        print('Not Available')
main()
