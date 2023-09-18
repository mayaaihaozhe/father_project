from pprint import pprint

def west_pp():
    data = 'this is data'
    for i in range(5):
        pprint(i)
        if i % 2 != 0:
            pprint(f'{i} is 偶数')


west_pp()