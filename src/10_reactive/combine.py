from rx import from_
from rx import operators as op

list1 = [23, 38, 43, 23]
list2 = [1, 2, 3, 4]
source1 = from_(list1)
source2 = from_(list2)
sources = [source1, source2]


def main():
    from_(sources).pipe(op.merge_all()).subscribe(lambda t: print(t))


if __name__ == '__main__':
    main()

'''
23
38
43
23
1
2
3
4
'''
