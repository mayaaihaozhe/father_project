from pprint import pprint


def west_pp():
    data = 'this is data'
    for i in range(len(data)):
        pprint(i)
        if i % 2 != 0:
            pprint(f'{i} is 偶数')



if __name__=='__main__':
    west_pp()
